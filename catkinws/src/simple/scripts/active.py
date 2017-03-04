#!/usr/bin/env python

from cros import *
import rospy

class Simple1(CROS):
    @base
    def test(self):
        print('base')

# XXX find better description
Simple1.add_layer('layer1')
Simple1.add_layer('layer2')

def test_l1(self):
    print('l1')

def test_l2(self):
    print('l2')
        
# XXX find better description
Simple1.add_method('layer1', 'test', test_l1)
Simple1.add_method('layer2', 'test', test_l2)


# Main
rospy.init_node('talker', anonymous=True)

a = Simple1()
a.activate(False)
r = rospy.Rate(1)
a.test()
a.activate('layer1')
r.sleep()
r.sleep()
a.test()
a.activate('layer2')
r.sleep()
a.test()

