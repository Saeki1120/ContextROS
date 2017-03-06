#!/usr/bin/env python
PKG='test1'
import unittest
from crospy import CROS, CPy, cpylayer, cpybase

class CPy1(CPy):
    def __init__(self):
        self.reset()
        CPy.__init__(self)

    def reset(self):
        self.base_called = False
        self.l1_called = False
        self.l2_called = False
        
    @cpybase
    def test(self):
        self.base_called = True

    @cpybase
    def skiptest(self):
        self.base_called = True

@cpylayer(CPy1, 'l1', 'test')
def test_l1(self):
    self.l1_called = True

@cpylayer(CPy1, 'l2', 'test')
def test_l2(self):
    self.l2_called = True
    self.proceed()
    
## A sample python unit test
class CPyTest(unittest.TestCase):
    def test_base_called(self):
        obj = CPy1()
        obj.test()
        self.assertEqual(True, obj.base_called)

    def test_activate_l1(self):
        obj = CPy1()
        obj.activate('l1')
        obj.test()
        self.assertEqual(False, obj.base_called)
        self.assertEqual(True, obj.l1_called)

    def test_actdeact_l1(self):
        obj = CPy1()
        obj.activate('l1')
        obj.test()
        
        obj.reset()
        
        obj.deactivate('l1')
        obj.test()
        self.assertEqual(True, obj.base_called)
        self.assertEqual(False, obj.l1_called)
        
    def test_activate_l1_l2(self):
        obj = CPy1()
        obj.activate('l1')
        obj.activate('l2')
        obj.test()
        self.assertEqual(False, obj.base_called)
        self.assertEqual(True, obj.l1_called) # proceed
        self.assertEqual(True, obj.l2_called)

    def test_actl1l2_deactl1(self):
        obj = CPy1()
        obj.activate('l1')
        obj.activate('l2')
        obj.test()
        
        obj.reset()
        
        obj.deactivate('l1')
        obj.test()
        self.assertEqual(True, obj.base_called) # proceed
        self.assertEqual(False, obj.l1_called)
        self.assertEqual(True, obj.l2_called)

    def test_basemethod_called_without_layers(self):
        obj = CPy1()
        obj.skiptest()
        self.assertEqual(True, obj.base_called)
        self.assertEqual(False, obj.l1_called)
        self.assertEqual(False, obj.l2_called)
        
    def test_activate_l2_and_base_called(self):
        obj = CPy1()
        obj.activate('l2')
        obj.skiptest()
        self.assertEqual(True, obj.base_called)
        self.assertEqual(False, obj.l1_called)
        self.assertEqual(False, obj.l2_called)
        
if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_CPy', CPyTest)
