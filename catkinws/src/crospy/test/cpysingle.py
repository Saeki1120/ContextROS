#!/usr/bin/env python

import unittest
import rospy
from crospy import CPySingle, cpylayer, cpybase

PKG = 'testcpy'


class CPy1(CPySingle):

    def __init__(self):
        self.reset()
        super(CPy1, self).__init__()

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


class CPy2(CPySingle):

    def __init__(self):
        self.reset()
        super(CPy2, self).__init__()

    @cpybase
    def test(self):
        pass


@cpylayer(CPy2, 'l1', 'test')
def test_c2l2(self):
    pass


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
        self.assertEqual(True, obj.l1_called)  # proceed
        self.assertEqual(True, obj.l2_called)

    def test_actl1l2_deactl1(self):
        obj = CPy1()
        obj.activate('l1')
        obj.activate('l2')
        obj.test()

        obj.reset()

        obj.deactivate('l1')
        obj.test()
        self.assertEqual(True, obj.base_called)  # proceed
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
    rospy.init_node('test', anonymous=True)
    rosunit.unitrun(PKG, 'test_CPy', CPyTest)
