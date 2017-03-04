#!/usr/bin/env python

from cros import *
import rospy

class Simple1(CROS):
    @base
    def test(self):
        print('base')

@layer(Simple1, 'layer1', 'test')
def test_l1(self):
    print('l1')

@layer(Simple1, 'layer2', 'test')
def test_l2(self):
    print('l2')

# Main
rospy.init_node('talker', anonymous=True)

r = rospy.Rate(0.5)

a = Simple1()
r.sleep()
a.activate('base')
a.test()
r.sleep()
a.activate('layer1')
a.test()
r.sleep()
a.activate('layer2')
a.test()


