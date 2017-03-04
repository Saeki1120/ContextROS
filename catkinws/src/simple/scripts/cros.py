import rospy
from std_msgs.msg import String

class CPy:
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
        self._proceed_funcs.extend([self.__class__.layers[l][func.__name__]
                                        for l in self._layer if l in self.__class__.layers])
        return self.proceed(*args, **kwargs)
    return inner

def cpylayer(cls, layer, name):
    def f(func):
        cls.add_method(layer, name, func)
    return f

class CROS(CPy):
    """ContextROS"""

    def __init__(self):
        CPy.__init__(self)
        # for activate
        topic = 'cros/activate'
        self.actpub = rospy.Publisher(topic, String, queue_size=10)
        self.actsub = rospy.Subscriber(topic, String, self.receive_activation)
        # for deactivate
        topic = 'cros/deactivate'
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
        
