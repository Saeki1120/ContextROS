#!/usr/bin/env python
PKG='cpyq'

import rospy
from crospy import CPyQ, cpylayer, cpybase

class CPyQ1(CPyQ):
    @cpybase
    def test(self):
        pass

@cpylayer(CPyQ1, 'l1', 'test')
def test_l1(self):
    self.l1_called = True

@cpylayer(CPyQ1, 'l2', 'test')
def test_l2(self):
    self.l2_called = True

class CPyQTest(object):
    def test_basic(self):
        pass

if __name__ == '__main__':
    import rosunit
    rospy.init_node('test_cpyq', anonymous=True)
    rosunit.unitrun(PKG, 'test_CPyQ', CPyQTest)



