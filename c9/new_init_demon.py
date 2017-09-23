# coding=utf-8

# the order of init and new
print u'----------------------------'
class A(object):
    def __new__(cls):
        print u'A.class __new__'
        return super(A, cls).__new__(cls)

    def __init__(self):
        print u'A.class __init__'
        self.a = u'a'


class B(A):
    def __new__(cls):
        print u'B.class __new__'
        return super(B, cls).__new__(cls)

    def __init__(self):
        print u'B.class __init__'
        self.b = u'b'
        super(B, self).__init__()


b = B()
print b.b


print u'----------------------------'
"""
    同个类中的__new__与__init__ 的总参数数量最好一致,其中必填参数的数量必须一致eg:  B.__new__ 与 B.__init__
    
    __new__中的参数不会传给__init__ , 我猜测只是各自拿一份copy而已.
    
    执行顺序:先__new__ 后 __init__
    
"""

class A(object):
    def __new__(cls, aa):
        print u'A.__new__ : '+unicode(aa)
        return super(A, cls).__new__(cls)  # aa, 看来new的参数不一定会影响__init__(当然 我也不敢保证不影响)

    def __init__(self, aa):
        print u'A.__init__ : '+unicode(aa)  # bb
        self.a = u'a'


class B(A):
    def __new__(cls):
        print u'B.__new__ : '+unicode(u'bb')  # bb
        return super(B, cls).__new__(cls, u'aa')

    def __init__(self, bb=None, bbb=None):
        self.b = u'b'
        print u'B.__init__ : '+unicode(bb)  # bb
        super(B, self).__init__(bb)

b = B()    # 不报错
# b = B(u'bb')    #报错, 因为b.__new__ 参数表不够
b2 = A.__new__(B, u'aa')

print b2    # 虽然是 B类型, 但是没有b属性
print hasattr(b, u'b')
print hasattr(b2, u'b')

