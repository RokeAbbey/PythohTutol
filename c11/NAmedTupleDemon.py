# coding=utf-8

u"""
	from collections import namedtuple
	Point = namedtuple(u'Point', [u'x', u'y', u'z'], verbose=True)
	p = tuple.__new__(Point, (1, 2, 3))
	print p
	print p.x, p.y, p.z
	help(Point.x)
"""


# my namedtuple
# 更多与__new__相关的请见c9 new_init_demon
class MyNameTuple(type):

    def __new__(self, name, fieldsname):     # ********2# 此处与***1处都需要3个参数(除了self), 否则报错
        d = {}
        _name = name
        d.fromkeys(fieldsname)
        for index, name in enumerate(fieldsname):
            d[name] = property(MyNameTuple.getProperty(index))

        d[u'__init__'] = tuple.__init__  # lambda _self, ars: tuple.__init__(_self, ars)

        print _name
        print d
        return super(MyNameTuple, self).__new__(self, 'from_new_'+_name, (tuple, ), d)
    # 这里重写了init, 为了不让*******2 与***1的错误发生, 因为init 与 new的参数数量需要一致, 如果不重写
    # 的话,那么就会调用type.__init__ 这样需要4个参数(算上self)

    def __init__(cls, name, fieldsname):
        super(MyNameTuple, cls).__init__('from_init_'+name, (tuple, ), fieldsname)


    @staticmethod
    def getProperty(index):
        def g(__self):
            __index = index
            #exec u'return __self[{index}]'.format(index=__index)
            return __self[__index]

        return g


Point = MyNameTuple('Point', ['x', 'y'])  #*******1
print Point

print Point([1, 2, 3]).x

