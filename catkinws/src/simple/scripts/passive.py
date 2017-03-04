#!/usr/bin/env python

from cros import *
import rospy

class Simple2(CROS):
    @base
    def test(self):
        print('base')

# XXX find better description
Simple2.add_layer('layer1')
Simple2.add_layer('layer2')

def test_l1(self):
    print('l1')

def test_l2(self):
    print('l2')
        
# XXX find better description
Simple2.add_method('layer1', 'test', test_l1)
Simple2.add_method('layer2', 'test', test_l2)

# Main
rospy.init_node('talker', anonymous=True)

a = Simple2()
r = rospy.Rate(1)
while not rospy.is_shutdown():
    a.test()
    r.sleep()
