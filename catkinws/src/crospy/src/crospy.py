import rospy
from crospy.srv import pub, sub, subResponse, pubResponse
from std_msgs.msg import String


class CPySingle(object):

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
        super(CPySingle, self).__init__()
        # array of activated layers
        self._layer = ['base']
        # array of valid functions for proceeds, init at method call
        self._proceed_funcs = []
        # cache
        self.purge_cache()

    def purge_cache(self):
        self.cache = {}

    def activate(self, layer):
        self.purge_cache()
        self._layer.append(layer)

    def deactivate(self, layer):
        self.purge_cache()
        self._layer.remove(layer)

    def proceed(self, *args, **kwargs):
        current = self._proceed_funcs.pop()
        retval = current(self, *args, **kwargs)
        self._proceed_funcs.append(current)
        return retval


def cpybase(func):
    def activated_funcs(self, fname):
        a = [func]  # for base
        try:
            a.extend([self.__class__.layers[l][fname]
                      for l in self._layer
                      if l in self.__class__.layers])
        except:
            pass
        return a

    def f(self, *args, **kwargs):
        fname = func.__name__
        if fname in self.cache:
            self._proceed_funcs = self.cache[fname]
        else:
            self._proceed_funcs = activated_funcs(self, fname)
            self.cache[fname] = self._proceed_funcs
        return self.proceed(*args, **kwargs)

    return f


def cpylayer(cls, layer, name):
    def f(func):
        cls.add_method(layer, name, func)
    return f


class CPy(CPySingle):
    instances = []

    def __init__(self):
        super(CPy, self).__init__()
        self.queued_request = []
        self.in_critical = False
        CPy.instances.append(self)

    @classmethod
    def activate(cls, layer):
        for i in CPy.instances:
            i.req_activate(layer)

    @classmethod
    def deactivate(cls, layer):
        for i in CPy.instances:
            i.req_deactivate(layer)

    def req_activate(self, layer):
        if self.in_critical:
            self.queued_request.append(('act', layer))
        else:
            super(CPy, self).activate(layer)

    def req_deactivate(self, layer):
        if self.in_critical:
            self.queued_request.append(('dea', layer))
        else:
            super(CPy, self).deactivate(layer)

    def begin(self):
        self.in_critical = True

    def end(self):
        self.do()
        self.in_critical = False

    def do(self):
        for r in self.queued_request:
            if r[0] == 'act':
                super(CPy, self).activate(r[1])
            elif r[0] == 'dea':
                super(CPy, self).deactivate(r[1])
        self.queued_request = []


class Critical(object):

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        self.obj.begin()

    def __exit__(self, type, value, traceback):
        self.obj.end()


class Layer(object):

    def __init__(self, layer):
        self.layer = layer

    def __enter__(self):
        CPy.activate(self.layer)

    def __exit__(self, type, value, traceback):
        CPy.deactivate(self.layer)


def crosyncsub(group=''):
    return 'cros/sync/' + group + 'sub'


def crosyncpub(node, group=''):
    return 'cros/sync/' + group + 'pub/' + str(node)


class CROSNode(object):
    _instance = None

    def __new__(cls, is_sync, node, group):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            # error check have to be done
            if is_sync:
                cls._instance.sync_init(node, group)
            else:
                cls._instance.async_init(group)

        return cls._instance

    def async_init(self, group):
        def handle_activate(data):
            if rospy.get_name() != data._connection_header['callerid']:
                CROS._activate_local(data.data)

        def handle_deactivate(data):
            if rospy.get_name() != data._connection_header['callerid']:
                CROS._deactivate_local(data.data)

        self.is_sync = False

        # for activate
        topic = 'cros/' + group + '/activate'
        self.actpub = rospy.Publisher(topic, String, queue_size=10)
        self.actsub = rospy.Subscriber(topic, String, handle_activate)
        # for deactivate
        topic = 'cros/' + group + '/deactivate'
        self.deactpub = rospy.Publisher(topic, String, queue_size=10)
        self.deactsub = rospy.Subscriber(topic, String, handle_deactivate)

    def sync_init(self, node, group):
        def handle_publish(data):
            if data.type == 'act':
                CROS._activate_local(data.layer)
            else:
                CROS._deactivate_local(data.layer)
            return pubResponse(0)

        self.is_sync = True

        # subscribe (from this to server)
        rospy.wait_for_service(crosyncsub(group))
        subscribe = rospy.ServiceProxy(crosyncsub(group), sub)
        subscribe(crosyncpub(node, group))
        # set publish (from this to server)
        rospy.wait_for_service(crosyncpub(0, group))
        self.crosync_publish = rospy.ServiceProxy(crosyncpub(0, group), pub)
        # receive publish (from server to this)
        rospy.Service(crosyncpub(node, group), pub, handle_publish)
        # save path
        self.crosync_path = (node, group)

    def send_activate(self, layer):
        if self.is_sync:
            self.crosync_publish('act', layer)
        else:
            self.actpub.publish(layer)

    def send_deactivate(self, layer):
        if self.is_sync:
            self.crosync_publish('dea', layer)
        else:
            self.deactpub.publish(layer)


class CROS(CPy):

    def __init__(self, is_sync=False, node='0', group=''):
        self.node = CROSNode(is_sync, node, group)
        super(CROS, self).__init__()

    # it activate the layer in the local classes
    # user should not call
    @classmethod
    def _activate_local(cls, layer):
        CPy.activate(layer)

    # it deactivate the layer in the local classes
    # user should not call
    @classmethod
    def _deactivate_local(cls, layer):
        CPy.deactivate(layer)

    # user can call this activation method
    def activate(self, layer):
        self.node.send_activate(layer)
        CROS._activate_local(layer)

    # user can call this dectivation method
    def deactivate(self, layer):
        self.node.send_deactivate(layer)
        CROS._deactivate_local(layer)


def crosyncserver(group=''):
    crossyncserver_client = []

    def handle_sub(req):
        callerid = req._connection_header['callerid']
        proxyobj = rospy.ServiceProxy(req.client, pub)
        crossyncserver_client.append((callerid, proxyobj))
        print('sub: ' + req.client)
        return subResponse(0)

    def handle_pub(req):
        callerid = req._connection_header['callerid']
        for c in [c[1] for c in crossyncserver_client if c[0] != callerid]:
            c(req.type, req.layer)
        return pubResponse(0)

    def server():
        print('server starting...')
        rospy.Service(crosyncsub(group), sub, handle_sub)
        print('service: ' + crosyncsub(group))
        rospy.Service(crosyncpub('0', group), pub, handle_pub)
        print('service: ' + crosyncpub(0, group))
        print('server started')
        rospy.spin()

    server()
