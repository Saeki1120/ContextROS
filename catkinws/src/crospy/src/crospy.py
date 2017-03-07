import multiprocessing
import rospy
from crospy.srv import pub, sub
from std_msgs.msg import String

class CPy(object):
    @classmethod
    def init_layer(cls):
        if not hasattr(cls, 'layers'):
            cls.layers = {}
    
    @classmethod
    def add_layer(cls, layer):
        cls.init_layer()
        cls.layers[layer] = {}

    @classmethod
    def add_method(cls, layer, name, method):
        cls.init_layer()
        if layer not in cls.layers:
            cls.add_layer(layer)
        cls.layers[layer][name] = method
        
    def __init__(self):
        # array of activated layers
        self._layer = ['base']
        # array of valid functions for proceeds, init at method call
        self._proceed_funcs = []

    def activate(self, layer):
        self._layer.append(layer)

    def deactivate(self, layer):
        self._layer.remove(layer)

    def proceed(self, *args, **kwargs):
        current = self._proceed_funcs.pop()
        retval = current(self, *args, **kwargs)
        self._proceed_funcs.append(current)
        return retval

def cpybase(func):
    def inner(self, *args, **kwargs):
        self._proceed_funcs = [func] # for base
        try:
            self._proceed_funcs.extend([self.__class__.layers[l][func.__name__]
                                            for l in self._layer if l in self.__class__.layers])
        except:
            pass
        return self.proceed(*args, **kwargs)
    return inner

def cpylayer(cls, layer, name):
    def f(func):
        cls.add_method(layer, name, func)
    return f

class CROS(CPy):
    """ContextROS"""

    def __init__(self, group=''):
        CPy.__init__(self)
        # for activate
        topic = 'cros/' + group + '/activate'
        print(topic)
        self.actpub = rospy.Publisher(topic, String, queue_size=10)
        self.actsub = rospy.Subscriber(topic, String, self.receive_activation)
        # for deactivate
        topic = 'cros/' + group + '/deactivate'
        self.deactpub = rospy.Publisher(topic, String, queue_size=10)
        self.deactsub = rospy.Subscriber(topic, String, self.receive_deactivation)

    def activate(self, layer):
        self.actpub.publish(layer)

    def deactivate(self, layer):
        self.deactpub.publish(layer)

    def receive_activation(self, data):
        CPy.activate(self, data.data)

    def receive_deactivation(self, data):
        CPy.deactivate(self, data.data)

def crosyncsub(group = ''):
    return 'cros/sync/' + group + 'sub'

def crosyncpub(node, group = ''):
    return 'cros/sync/' + group + 'pub/' + str(node)

class CROSync(CPy):
    def __init__(self, node='0', group=''):
        def handle_pub(data):
            return self.handle_pub(data)
        
        CPy.__init__(self)
        self.group = group
        # subscribe
        rospy.wait_for_service(crosyncsub(group))
        subscribe = rospy.ServiceProxy(crosyncsub(group), sub)
        subscribe(crosyncpub(node, group))
        # set publish
        rospy.wait_for_service(crosyncpub(group))
        self.publish = rospy.ServiceProxy(crosyncpub(group), pub)
        rospy.Service(crosyncpub(node, group), pub, handle_pub)

    def activate(self, layer):
        self.publish('act', layer)

    def deactivate(self, layer):
        self.publish('dea', layer)

    def handle_pub(self, data):
        if data.type == 'act':
            self.receive_activation(self, data.layer)
        else:
            self.receive_deactivation(self, data.layer)
    
    def receive_activation(self, layer):
        CPy.activate(self, layer)

    def receive_deactivation(self, layer):
        CPy.deactivate(self, layer)

crossyncserver_client = []
crossyncserver_p = False
def crosyncserver(group=''):
    def handle_sub(req):
        name = crosyncpub(req.client, group)
        crossyncserver_client.append(rospy.ServiceProxy(name, pub))
        req.ret = 0

    def handle_pub(req):
        for c in crossyncserver_client:
            c(req.type, req.layer)
        req.ret = 0

    def server():
        print('server starting...')
        rospy.Service(crosyncsub(group), sub, handle_sub)
        print('service: ' + crosyncsub(group))
        rospy.Service(crosyncpub('0', group), pub, handle_pub)
        print('service: ' + crosyncpub(0, group))
        print('server started')
        rospy.spin()

    crossyncserver_p = multiprocessing.Process(target=server)
    crossyncserver_p.start()

def croserver_kill():
    crossyncserver_p.terminate()
    #crossyncserver_p.join()
