#coding=utf-8
import math
print u'cos(pi) = {}'.format(math.cos(math.pi))
print u'acos(0) = {}'.format(math.acos(0))
print u'log(1024, 2) = {}'.format(math.log(1024, 2))

import random
print u'random.sample() : {}'.format(random.sample(xrange(0, 100), 6))
print u'random.choice() : {}'.format(random.choice(xrange(0, 100)))
print u'random.random() : {}'.format(random.random())
print u'random.randrange() : {}'.format(random.randrange(start=6, stop=10, step=1))
#random.randrange(6):那就从0-6中选, 此时start = 6 ,如果同时规定Start 与stop 那么就从两者之间选择
