# coding=utf-8
class A(object):
    def __getx(self):
        print u'get'
        return self.__x

    def __setx(self, newX):
        self.__x = newX

    def __delx(self):
        del self.__x

    x = property(__getx, __setx, __delx, doc=u'test of property')

a = A()
a.x
a.x = 1
print a.x

u'''
    可以看看NamedTupleDemon中自己写的namedtuple
'''