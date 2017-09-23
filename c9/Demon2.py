#coding=utf-8

'''
class _cls1(object):
    lst = []
    def __init__(cls, item=None, tailList=None):
        if item:
            cls.lst.append(item)

        if tailList:
            cls.lst.extend(tailList)

        print cls.lst

class cls2:
    __metaclass__ = _cls1

    def __init__(self, template):
        self.template = template

    def test(self):
        print self.lst

a = cls2(u'abcdefg')
a.test()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''
import sys

def test(depth = 0):
    frame = sys._getframe(depth)
    code = frame.f_code

    print "frame depth = ", depth
    print "func name = ", code.co_name
    print "func filename = ", code.co_filename
    print "func lineno = ", code.co_firstlineno
    print "func locals = ", frame.f_locals

def main():
    test(0)
    print "--------"
    test(1)
    print u'--------'
    test(2)
    print u'--------'
    test(3)
def outter():
    main()

if __name__ == "__main__":
    outter()

'''
#元类

#example 1

print u'---------------------example1'

def upper_attr(class_name, class_parents, class_attr):
    """
    返回一个对象,将属性都改为大写的形式
    :param class_name:  类的名称
    :param class_parents: 类的父类tuple
    :param class_attr: 类的参数
    :return: 返回类
    """
# 生成了一个generator
    print u' involk upper_attr'
    u"""
        如果__metaclass__ 在module层, 那么Foo 与 FooP的类属性不会在class_attr中登记
        如果__metaclass__ 在FooP层面, 那么FooP中的属性可以进入到class_attr中, 但是Foo中的属性不会
        ....__metaclass__...Foo层面,那么Foo中的属性可在class_attr中登记, FooP中的不会
    """
    print u'class_name : {0}\n class_parents : {1}\n class_attr : {2}'.format(class_name, class_parents, class_attr)

    attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
    uppercase_attrs = dict((name.upper(), value) for name, value in attrs)
    return type(class_name, class_parents, uppercase_attrs)

#__metaclass__ = upper_attr
class FooP(object):
#    __metaclass__ = upper_attr
    fooPBar = u'bip'
    pass

class Foo(FooP):
    __metaclass__ = upper_attr
    bar = u'bip'
pw = Foo()
print hasattr(pw, 'bar')
print hasattr(pw, 'BAR')

print hasattr(pw, u'fooPBar')
print hasattr(pw, u'FOOPBAR')
#print pw.BAR

#output:
#False
#True

#example2
print u'---------------------example2'
class MetaA(type):
    def __new__(cls, clsName, bases, fields):
        print u'cls : {0},\nclsName : {1},\nbases : {2},\nfields : {3}'.format(cls, clsName, bases, fields)
        fields = dict(((x.upper(), y) for x, y in fields.items() if not x.startswith(u'__')))
        return super(MetaA, cls).__new__(cls, clsName, bases, fields)

class AP(object):
    ap = 2
    def __init__(self):
        pass
class A(AP):
    a = 1
    __metaclass__ =  MetaA
    def __init__(self, b=None, c=None):
        self.b = b
        self.c = c

a = A()
print hasattr(a, u'a')
print hasattr(a, u'A')

print hasattr(a, u'b')
print hasattr(a, u'B')

print hasattr(a, u'c')
print hasattr(a, u'C')

print hasattr(a, u'ap')
print hasattr(a, u'AP')

