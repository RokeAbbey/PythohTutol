#coding=utf-8
print __name__
import traceback
import sys

#from ..c9 import Module1
#from ..c7.Class import Class as cls
#from ..c7.Student import Student as stu

# part1
'''
class C(object):
    maxId = 0
    def __init__(self):
        self._id = C.maxId
        C.maxId += 1

    def g(self, a, b):
        print self._id
        return a + b

    h = g

    @classmethod
    def increaseMaxId(cls):
        cls.maxId += 1

if __name__ == '__main__':
    c = C()
    print c.g(1, 2)
    print c.h(1, 2)

    C.increaseMaxId()
    c = C()
    print c.g(1, 2)
    print c.h(1, 2)

'''

#mutiple inheritance and private field
#'''
class A(object):
    def __init__(self):
        print u'enter A'
        super(A, self).__init__()
        print u'out A'

class B(object):
    def __init__(self):
        print u'enter B'
        super(B, self).__init__()
        print u'out B'

class C(A, B):
    def __init__(self):
        print u'enter C'
        super(C, self).__init__()
        print u'out C'

class D(B):
    def __init__(self):
        print u'enter D'
        super(D, self).__init__()
        print u'out D'

class E(C, D):
    def __init__(self):
        print u'enter E'
        super(E, self).__init__()
        print u'out E'

class F(A):
    __className = u'F'
    def __init__(self):
        print u'enter F'
        super(F, self).__init__()
        print u'out F'

class G(F, E, D):
    __className = u'G'
    def __init__(self):
        self.__id = 0
        print u'enter G'
        super(G, self).__init__()
        print u'out G'

g = G()
#'''
'''
    enter G
    enter F
    enter E
    enter C
    enter A
    enter D
    enter B

    out B,D,A,C,E,F,G
'''
'''
print G.__dict__
print g.__dict__
try:
    print G.__className

except AttributeError as atberror:
    exc_name, exc_value, exc_tb = sys.exc_info()
    traceback.print_exception(exc_name, exc_value, exc_tb)

print G._G__className
print g._G__className           #g.__className也不行


print g._G__id                  #g.__id 也不行


g.__name = 'roke'
print g.__name
#print g._G__name                #报错
'''


#iterators
'''
stu1 = stu('Roke', 100)
stu2 = stu('Lou', 0)
stu3 = stu('Fei', 60)
students = [stu1, stu2, stu3]
myClass = cls('软件工程1401', students)
for st in myClass:
    print st
'''







