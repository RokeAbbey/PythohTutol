#coding=utf-8
import re
if __name__ == u'__main__':
    print u'------------------------------'
    s = u'hello pan'
    p = re.compile(u'(.*)(lo)(.*)(p)(.*)')
    print p.sub(ur'\1\4\3\2\5', s)

    print p.sub(lambda m: m.group(1)+m.group(4)+m.group(3)+m.group(2)+m.group(5), s)
    print u''

    print u'------------------------------'
    s = u'hello _123_ pan'
    r = u'(\d{3})|(\w{3}$)'
    p = re.compile(r)
    m = p.findall(s)
    print m
    print p.search(s).group(2)
    # print p.sub(ur' \2 ok ', s) #注意看正则表达式\1是匹配不到的,所以在sub的第一个参数如果使用\1的话会有异常抛出,如果将正则表达式的\d{4} 改成{3},那么s中一共有两处可以取到,分别是\1(123) 和 \2(pan), 但是两者又不能同时取到,因为有'|',所以如果想用Sub改变s的话,最好用函数, 如下
    def subFun (m):
        n = 0
        if m.group(1):
            n = 1
        elif m.group(2):
            n = 2
        return u'm.group({num}) is {group}{0}'.format(u'.', num=n, group=m.group(n))

    print p.sub(subFun, s)
