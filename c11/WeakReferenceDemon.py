# coding=utf-8


import weakref, gc

class A(object):
    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return self.__value


a = A(u'hello')
b = a
del a
gc.collect()

print b

d = weakref.WeakValueDictionary()
d['a'] = b
del b
gc.collect()
print d[u'a']  # 无法再次输出hello

'''
a = A(u'abc')
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

d['primary']
'''


