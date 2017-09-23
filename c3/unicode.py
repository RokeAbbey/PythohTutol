#coding=gbk
import sys

print 'system default encoding = ' + str(sys.getdefaultencoding())
a = '我的'
print 'a\'s type is ' + str(type(a))
print a

b =  u'我的'
print 'b\'s type is ' + str(type(b))
print b

c =  a.decode('gbk')
print 'c\'s type is ' + str(type(c))
print c

d =  c.encode('gbk')
print 'd\'s type is ' + str(type(d))
print d

e = b.encode('gbk')
print 'e\'s type is ' + str(type(e))
print e



f = unicode(a,'gbk')
print 'f\'s type is ' + str(type(f))
print f
