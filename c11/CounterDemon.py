# coding=utf-8
# Counter
# example of Counter(), elements, most_common, sub_tract, update
from collections import Counter


print u'--------------------------'
cnt = Counter([u'aa', u'a', u'bb', u'b', u'aa', u'b', u'b'])
print cnt
print list(cnt.elements())
print cnt.most_common(3)  # bb 与 a的次数一样,但是只打印a的 估计是乱序, 据我观察也不是字典序

cnt2 = Counter((u'aa', u'a', u'bb'))
cnt.subtract(cnt2)
print u'after subtract = {}'.format(cnt)

cnt = Counter({u'aa': 15, u'bb': 10, u'c': 100})
cnt2 = Counter({u'bb': 20, u'dd': 30})
cnt.subtract(cnt2)
print u'after subtract = {}'.format(cnt)
cnt.update(cnt2)
print u'after update = {}'.format(cnt)

# more example about subtract and update
print u'--------------------------'
from collections import Counter
import pprint
cnt = Counter({u'a': 10, u'b': 20})
gen = (u'a' for x in xrange(20))
cnt.subtract(gen)

print u'after subtract cnt = {}'.format(cnt)

li = [u'b' for x in xrange(20)]
cnt.subtract(li)
print u'after subtract cnt = {}'.format(cnt)

# example of Counter
print u'----------------------------'

from collections import Counter
import urllib2

url = urllib2.urlopen(u'http://www.baidu.com')
li = []
for line in url:
    li.append(line)
li = [x.decode(u'utf-8') for x in li]
context = u'\n'.join(li)
print u'context are {}'.format(context)
cnt = Counter(li)

pp = pprint.PrettyPrinter(width=80, indent=4)

print u'first 10 common words in baidu.com are {}'\
    .format(pp.pformat(cnt.most_common(10)))



# example of counter's add and sub
# 注意 subtrace 后的结果 0 与 负数都保留下来, 但是 - 之后的结果 只保留正整数, 加法类似
print u'------------------------'

from collections import Counter
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)

cnt = Counter(u'abbbc')
cnt2 = Counter(u'aaabc')
result = {
    u'cnt': cnt,
    u'cnt2': cnt2,
    u'cnt - cnt2': cnt - cnt2,
    u'len(cnt - cnt2)': len(cnt - cnt2),
}
presult = pp.pformat(result)    # 在subtract之间先打印一次, 因为sub会改变cnt
print u'"-" : \n'+presult
print u''
cnt.subtract(cnt2)    # 请注意 字典中引用的是一个地址, 并不是值, 所以此处sub 上面result中的cnt会变化
result[u'cnt.subtract(cnt2)'] = cnt

presult = pp.pformat(result)
print presult
"""
pcnt = pp.pformat(cnt)
pcnt2 = pp.pformat(cnt2)
print u'before sub : cnt = \n{}, \ncnt2 = \n{}'.format(pcnt, pcnt2)
print u'after sub : cnt - cnt2 = {}, \nlen = {}, \ncnt = {}, \ncnt2 = {}'\
    .format(pp.pformat(cnt - cnt2), len(cnt - cnt2), pcnt, pcnt2)

"""

cnt = Counter({u'a': -10, u'b': -1})
cnt2 = Counter({u'a': -10, u'b': 5, u'c': 10})

result = {
    u'cnt': cnt,
    u'cnt2': cnt2,
    u'cnt + cnt2': cnt + cnt2,
    u'len(cnt + cnt2)': len(cnt + cnt2)
}
presult = pp.pformat(result)
print u'"+" : \n'+presult
"""
pcnt = pp.pformat(cnt)
pcnt2 = pp.pformat(cnt2)
print u'before add : cnt = \n{}, cnt2 = \n{}'.format(pcnt, pcnt2)
print u'after add : cnt + cnt2 = {}, \nlen = {}, \ncnt = {}, \ncnt2 = {}'\
    .format(pp.pformat(cnt + cnt2), len(cnt + cnt2), pcnt, pcnt2)


"""
