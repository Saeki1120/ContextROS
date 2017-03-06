#!/usr/bin/env python
PKG='test1'
import unittest
import rospy
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

class CPy2(CPy): 
    def __init__(self):
        self.reset()
        CPy.__init__(self)

    @cpybase
    def test(self):
        pass

@cpylayer(CPy2, 'l1', 'test')
def test_c2l2(self):
    pass
    
## A sample python unit test
class CPyTest(unittest.TestCase):
    def test_check_layers(self):
        self.assertEqual(set(['l1', 'l2']), set(CPy1.layers.keys()))

    def test_check_layers2(self):
        # confirm CPy1 and CPy2 are not contaminated each other
        self.assertEqual(set(['l1']), set(CPy2.layers.keys()))
        
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

class CROS1(CROS):
    def __init__(self):
        self.reset()
        CROS.__init__(self)

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

@cpylayer(CROS1, 'l1', 'test')
def test_1l1(self):
    self.l1_called = True

@cpylayer(CROS1, 'l2', 'test')
def test_1l2(self):
    self.l2_called = True
    self.proceed()
    
class CROS2(CROS1):
    pass
    
@cpylayer(CROS2, 'l1', 'test')
def test_2l1(self):
    self.l1_called = True

@cpylayer(CROS2, 'l2', 'test')
def test_2l2(self):
    self.l2_called = True
    
class CROSTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CROSTest, self).__init__(*args, **kwargs)
        self.r = rospy.Rate(1)

    def sleep(self):
        self.r.sleep()
        
    def test_base_called(self):
        c1 = CROS1()
        c2 = CROS2()
        c1.test()
        c2.test()
        self.assertEqual(True, c1.base_called)
        self.assertEqual(True, c2.base_called)

    def test_l1_active(self):
        c1 = CROS1()
        c2 = CROS2()
        self.sleep() # need to subscribe...
        c1.activate('l1')
        self.sleep()
        c1.test()
        c2.test()
        self.assertEqual(True, c1.l1_called)
        self.assertEqual(True, c2.l1_called)
        
if __name__ == '__main__':
    import rosunit
    rospy.init_node('test', anonymous=True)
    rosunit.unitrun(PKG, 'test_CPy', CPyTest)
    rosunit.unitrun(PKG, 'test_CROS', CROSTest)
