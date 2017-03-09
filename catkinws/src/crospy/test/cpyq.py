#!/usr/bin/env python
PKG='cpyq'

import unittest
import rospy
from crospy import CPyQ, cpylayer, cpybase, Layer, Critical

class CPyQ1(CPyQ):
    def __init__(self):
        CPyQ.__init__(self)
        self.base_callee_called = False
        self.l1_callee_called = False
        self.l2_callee_called = False

    @cpybase
    def callee(self):
        self.base_callee_called = True

@cpylayer(CPyQ1, 'l1', 'callee')
def callee_l1(self):
    self.l1_callee_called = True

@cpylayer(CPyQ1, 'l2', 'callee')
def callee_l2(self):
    self.l2_callee_called = True

class CPyQTest(unittest.TestCase):
    def test_basic(self):
        obj = CPyQ1()
        
        with Critical(obj):
            obj.activate('l1')
            obj.callee() # still base
            self.assertEqual(False, obj.l1_callee_called)
            self.assertEqual(True, obj.base_callee_called)
            
            obj.activate('l2')
            obj.callee() # still base
            self.assertEqual(False, obj.l1_callee_called)
            self.assertEqual(True, obj.base_callee_called)

            obj.deactivate('l2')
            obj.callee() # of course still base
            self.assertEqual(False, obj.l1_callee_called)
            self.assertEqual(True, obj.base_callee_called)

            # check queue contents
            self.assertEqual([('act', 'l1'), ('act', 'l2'), ('dea', 'l2')], obj.queued_request)

        self.assertEqual(['base', 'l1'], obj._layer)
        obj.callee() # activated l1, deactivated l2
        self.assertEqual(True, obj.l1_callee_called)
        self.assertEqual(False, obj.l2_callee_called)

if __name__ == '__main__':
    import rosunit
    rospy.init_node('test_cpyq', anonymous=True)
    rosunit.unitrun(PKG, 'test_CPyQ', CPyQTest)
