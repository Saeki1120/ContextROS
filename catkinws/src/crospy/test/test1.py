#!/usr/bin/env python

import unittest
import rospy
from crospy import CROS, CROSync, CPy, cpylayer, cpybase

PKG = 'test1'


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
        self.sleep()  # need to subscribe...
        c1.activate('l1')
        self.sleep()
        c1.test()
        c2.test()
        self.assertEqual(True, c1.l1_called)
        self.assertEqual(True, c2.l1_called)

    def test_l1l2_active(self):
        c1 = CROS1()
        c2 = CROS2()
        self.sleep()  # need to subscribe...
        c1.activate('l1')
        c1.activate('l2')
        self.sleep()
        self.sleep()
        self.assertEqual(['base', 'l1', 'l2'], c1._layer)
        self.assertEqual(['base', 'l1', 'l2'], c2._layer)
        c1.test()
        c2.test()
        self.assertEqual(False, c1.l1_called)
        self.assertEqual(True, c1.l2_called)
        self.assertEqual(False, c2.l1_called)
        self.assertEqual(True, c2.l2_called)


class CROSync1(CROSync):

    def __init__(self, n):
        CROSync.__init__(self, n, '')
        self.reset()

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


@cpylayer(CROSync1, 'l1', 'test')
def test_3l1(self):
    self.l1_called = True


@cpylayer(CROSync1, 'l2', 'test')
def test_3l2(self):
    self.l2_called = True
    self.proceed()


class CROSync2(CROSync1):
    pass


@cpylayer(CROSync2, 'l1', 'test')
def test_4l1(self):
    self.l1_called = True


@cpylayer(CROSync2, 'l2', 'test')
def test_4l2(self):
    self.l2_called = True


class CROSyncTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(CROSyncTest, self).__init__(*args, **kwargs)

    def test_base_called(self):
        c1 = CROSync1(1)
        c2 = CROSync2(2)
        c1.test()
        c2.test()
        self.assertEqual(True, c1.base_called)
        self.assertEqual(True, c2.base_called)

    def test_l1_active(self):
        c1 = CROSync1(3)
        c2 = CROSync2(4)
        c1.activate('l1')
        c1.test()
        c2.test()
        self.assertEqual(True, c1.l1_called)
        self.assertEqual(True, c2.l1_called)

    def test_l1l2_active(self):
        c1 = CROSync1(5)
        c2 = CROSync2(6)
        c1.activate('l1')
        c1.activate('l2')
        c1.test()
        c2.test()
        self.assertEqual(['base', 'l1', 'l2'], c1._layer)
        self.assertEqual(['base', 'l1', 'l2'], c2._layer)
        self.assertEqual(False, c1.l1_called)
        self.assertEqual(True, c1.l2_called)
        self.assertEqual(False, c2.l1_called)
        self.assertEqual(True, c2.l2_called)


if __name__ == '__main__':
    import rosunit
    rospy.init_node('test', anonymous=True)
    rosunit.unitrun(PKG, 'test_CPy', CPyTest)
    rosunit.unitrun(PKG, 'test_CROS', CROSTest)
    rosunit.unitrun(PKG, 'test_CROSync', CROSyncTest)
