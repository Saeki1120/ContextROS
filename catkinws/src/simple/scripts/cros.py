import rospy
from std_msgs.msg import String

class CPy:
    @classmethod
    def add_layer(cls, layer):
        if not hasattr(cls, 'layers'):
            cls.layers = {}
        cls.layers[layer] = {}

    @classmethod
    def add_method(cls, layer, name, method):
        cls.layers[layer][name] = method
        
    def __init__(self):
        self._layer = 'base'

    def _activate(self, layer):
        self._layer = layer

def base(func):
    def inner(self, *args, **kwargs):
        if self._layer == 'base':
            return func(self, *args, **kwargs)
        else:
            return self.__class__.layers[self._layer][func.__name__](self, *args, **kwargs)
    return inner

class CROS(CPy):
    """ContextROS"""

    def __init__(self):
        CPy.__init__(self)
        self.topic = 'cros/activate'
        self.publisher = rospy.Publisher(self.topic, String, queue_size=10)
        self.sbscriber = rospy.Subscriber(self.topic, String, self.receive_activation)

    def activate(self, layer):
        #self._activate(layer)
        self.publisher.publish(layer)

    def receive_activation(self, data):
        print('receive: ' + data.data)
        self._activate(data.data)
        
