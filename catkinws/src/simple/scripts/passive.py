#!/usr/bin/env python

from cros import *
import rospy

class Simple2(CROS):
    @base
    def test(self):
        print('base')

@layer(Simple2, 'layer1', 'test')
def test_l1(self):
    print('l1')
    self.proceed()

@layer(Simple2, 'layer2', 'test')
def test_l2(self):
    print('l2')
    
# Main
rospy.init_node('talker', anonymous=True)

a = Simple2()
r = rospy.Rate(1)
while not rospy.is_shutdown():
    a.test()
    r.sleep()
