#!/usr/bin/env python
PKG='perfeval'

import unittest
import rospy
from crospy import CPy, cpylayer, cpybase
import cProfile

def test_nolayer_activated(N, o):
    for i in range(0, N):
        o.test()

def test_layer1_activated(N, o):
    o.activate('l1')
    for i in range(0, N):
        o.test()

def test_layer1_2_activated(N, o):
    o.activate('l1')
    o.activate('l2')
    for i in range(0, N):
        o.test()

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

class CPyCached(CPy):
    def __init__(self):
        CPy.__init__(self)
        self.cache = {}

    def activate(self, layer):
        self.cache = {}
        CPy.activate(self, layer)

    def deactivate(self, layer):
        self.cache = {}
        CPy.deactivate(self, layer)
        
def cpybasecached(func):
    def activated_funcs(self, fname):
        a = [func] # for base
        try:
            a.extend([self.__class__.layers[l][fname]
                          for l in self._layer if l in self.__class__.layers])
        except:
            pass
        return a
    
    def inner(self, *args, **kwargs):
        fname = func.__name__
        if fname in self.cache:
            self._proceed_funcs = self.cache[fname]
        else:
            self._proceed_funcs = activated_funcs(self, fname)
            self.cache[fname] = self._proceed_funcs
        return self.proceed(*args, **kwargs)
    return inner

class CPy2(CPyCached):
    def __init__(self):
        self.reset()
        CPyCached.__init__(self)

    def reset(self):
        self.base_called = False
        self.l1_called = False
        self.l2_called = False
        
    @cpybasecached
    def test(self):
        self.base_called = True

    @cpybasecached
    def skiptest(self):
        self.base_called = True

@cpylayer(CPy2, 'l1', 'test')
def test2_l11(self):
    self.l1_called = True

@cpylayer(CPy2, 'l2', 'test')
def test2_l2(self):
    self.l2_called = True
    self.proceed()
        
def run_test(name, func, obj):
    print(name, func)
    cProfile.run(func + '(100000, ' + obj + ')')
        
if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    run_test('baseline:', 'test_nolayer_activated', 'CPy1()')
    run_test('baseline:', 'test_layer1_activated', 'CPy1()')
    run_test('baseline:', 'test_layer1_2_activated', 'CPy1()')
    
    run_test('cached:', 'test_nolayer_activated', 'CPy2()')
    run_test('cached:', 'test_layer1_activated', 'CPy2()')
    run_test('cached:', 'test_layer1_2_activated', 'CPy2()')

    
