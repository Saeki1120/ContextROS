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
        self._layer = ['base']

    def _activate(self, layer):
        self._layer.append(layer)

    def _deactivate(self, layer):
        self._layer.remove(layer)

def base(func):
    def inner(self, *args, **kwargs):
        current_layer = self._layer[-1]
        if current_layer == 'base':
            return func(self, *args, **kwargs)
        else:
            return self.__class__.layers[current_layer][func.__name__](self, *args, **kwargs)
    return inner

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
        self._activate(data.data)

    def receive_deactivation(self, data):
        self._deactivate(data.data)
        
def layer(cls, layer, name):
    def f(func):
        cls.add_method(layer, name, func)
    return f
