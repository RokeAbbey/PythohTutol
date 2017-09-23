#coding=utf-8
import timeit
print u'-----------1-------'
print timeit.timeit(u'c in s', setup=u'c = u"o"; s = u"helloworld"', number=10000)
print timeit.timeit(u's.find(c)', setup=u'c = u"o"; s = u"helloworld"', number=10000)

print u'-----------2-------'
print timeit.timeit(u'u"hello {}{}{}{}{}{}".format(name, name, name, name, name, name)'
                    , setup=u'name = u"Roke"', number=10000)
print timeit.timeit(u'u"hello %s%s%s%s%s%s" % (name,name, name, name, name, name)'
                    , setup=u'name = u"Roke"', number=10000)
print timeit.timeit(u'u"hello "+name+name+name+name+name+name'
                    , setup=u'name = u"Roke"', number=10000)

print u'-----------3-------'

#abc = object()
s = \
"""
try:
    abc.abc

except AttributeError as ae:
    pass
"""

s2 = "if hasattr(abc, \"abc\") : pass"

print timeit.timeit(stmt=s, setup=\
u'''
class A(object):pass
abc = A()
'''
                    , number=10000)
print timeit.timeit(stmt=s2, setup=\
u'''
class A(object):pass
abc = A()
'''
                    ,number=10000)

print timeit.timeit(stmt=s, setup=\
u'''
class A(object):pass
abc = A()
abc.abc = None
'''
                    , number=10000)
print timeit.timeit(stmt=s2, setup=\
u'''
class A(object):pass
abc = A()
abc.abc = None
'''
                    , number=10000)

print u'-----------4-------'
def test(): return 1
test1 = lambda : 1
print  __name__
print timeit.timeit(u'test()', setup=u'from __main__ import test', number=10000)
print timeit.timeit(u'test1()', setup=u'from __main__ import test1', number=10000)
'''
def test():
        """Stupid test function"""
        L = []
        for i in range(100):
            L.append(i)
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
'''
