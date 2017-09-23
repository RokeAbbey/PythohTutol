# coding=utf-8
from collections import deque

u'''
example of deque's methods: 
    append, appendleft, pop, popleft, remove, reverse, rotate, count, clear, extend, extendleft
'''
d = deque(maxlen=5)
[d.append(x) for x in xrange(4)]
print u'd = {}'.format(d)
d.append(4)
d.append(5)
print u'd = {}'.format(d)   #the left elem '0' is disappeared

# d.maxlen = 10  #不可修改 会抛出异常
d = deque(d, maxlen=20)
d.extend((x for x in xrange(6, 10)))
print u'd = {}'.format(d)

[d.appendleft(x) for x in xrange(0, -5, -1)]
print u'd = {}'.format(d)

d.extendleft((x for x in xrange(-5, -10, -1)))
print u'd = {}'.format(d)

[d.pop() for x in xrange(5)]    # pop中没有参数 这里与list不一致
print u'd = {}'.format(d)

[d.popleft() for x in xrange(5)]    # 没有参数
print u'd = {}'.format(d)

d.rotate(2)
print u'd = {}'.format(d)

d.reverse()
print u'd = {}'.format(d)

d.reverse()
d.rotate(-2)
print u'd = {}'.format(d)


# deque recipes
print u'-------------------------------------'

print u'-----tail---'
def tail(filename, n=None):
    with open(filename) as f:
        return deque(f.read(), n)


'''
with open(u'file3.dat', u'a+') as f:
    for x in xrange(10):
        f.write(unicode(x) * x + u'\n')

'''
print tail(u'file3.dat', 3)  # 会打印出最后三个字符 而不是最后三行, 文档中说是三行


def tail2(filename, n=None):
    with open(filename) as f:
        return deque(f.readlines(), n)


print tail2(u'file3.dat', 3)  # 会打印出最后三行字符


print u'------moving average-----'

import itertools


def getMovingAverage(iterable, windowSize):
    it = iter(iterable)
    d = deque(itertools.islice(it, windowSize - 1), windowSize)
    d.appendleft(0)
    s = sum(d)
    result = deque()
    for v in it:
        s += v - d.popleft()
        result.append(s / float(windowSize))
        d.append(v)

    return result


print getMovingAverage([40, 30, 50, 46, 39, 44], 3)

print u'----------delete_nth----'


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)


d = deque((x for x in xrange(5, 10)))
delete_nth(d, 2)
print d
