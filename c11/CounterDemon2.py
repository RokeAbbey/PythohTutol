# coding=utf-8
from collections import Counter
from pprint import PrettyPrinter

class A(object):
    def __init__(self, value):
        self.__value = value

    def __repr__(self):
        return u'A_{}'.format(unicode(self.__value))

    def __str___(self):
        return 'A_{}'.format(str(self.__value))

    def __add__(self, other):
        if type(other) is int:
            return A(self.__value + other)
        return A(self.__value + other.__value)

    def __sub__(self, other):
        if type(other) is int:
            return A(self.__value - other)
        return A(self.__value - other.__value)

    def __cmp__(self, other):
        result = 0
        if type(other) is int:
            other = A(other)
        if self.__value < other.__value:
            result = -1
        elif self.__value > other.__value:
            result = 1
        return result


# example of A
"""
a = A(10)
a2 = A(20)

result = {
    u'a': a,
    u'a2': a2,
    u'a + a2': a + a2,
    u'a - a2': a - a2,
    u'cmp(a, a2)': cmp(a, a2)

}
pp = PrettyPrinter(indent=4, width=10)
presult = pp.pformat(result)
print u'result : \n{}'.format(presult)
"""
cnt = Counter(dict(
    (x, A(y)) for x in xrange(5) for y in xrange(x+5)
))
cnt2 = Counter(dict(
    (x, A(y)) for x in xrange(-3, 2) for y in xrange(x + 5)
))
# for elem, value in cnt.items():
#    print u'other["elem"] {0:>25}'.format(type(value))

# print type(cnt2)
result = {
    u'cnt': cnt,
    u'cnt2': cnt2,
    u'cnt - cnt2': cnt - cnt2,
    u'cnt + cnt2': cnt + cnt2
}
pp = PrettyPrinter(indent=4, width=80)
print u'result = '
pp.pprint(result)

