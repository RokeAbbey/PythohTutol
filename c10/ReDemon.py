#coding=utf-8
import re
import json
import os
'''
s = u'hello world world'
r = ur'.*([a-z])\1'
print re.match(r, s)
'''

#note : match好像不能匹配(?<=xxxx)的字符串,如果xxx不为空的话.有待验证,只是偶然碰巧碰到而已.因为这种模式是不消耗前面的字符串的
print u'the pwd = {}'.format(os.system(u'pwd'))#若不在本文件所在文档执行本脚本的话, 会出现input.dat找不到的情况
print u'the ls = {}'.format(os.system(u'ls'))#
if __name__ == '__main__':
    with open(u'input.dat', u'r') as f:
        l = []
        for line in f:
            l.append(line)
        js = ''.join(l)

print js
#just review the json.loads
'''
    myDict = json.loads(l)
    print myDict
'''
#get name
#   ----search
r = ur'"name":"(\w*)"'
p = re.compile(r)
m = p.search(js)
print u"search {}".format(m.group(1))
#   ----match
#正则表达式:在[] 中,所有特殊字符都失去特殊含义, 比如".", 本来是匹配除了'\n'之外的所有字符,结果成了真正的'.'

p = re.compile(ur'[\s\S]*{}'.format(r), re.M)#注意re.M是多行模式,但是不会影响\n\r等的匹配,仅仅影响$,^这两个运算符
#print p.pattern
m = p.match(js)
print u'match {}'.format(m.group(1))


#get age
#p = re.compile(ur'"age":(\d)*')  这样只会匹配一个字符, 哪怕age字段为11 22 这种相同的字符,也是只匹配一个
#   ----search
p = re.compile(ur'(?<="age":)(\d*)')
m = p.search(js)
print u'search {}'.format(m.group(1))

#   ----match
p = re.compile(ur'[\s\S]*(?<="age":)(?P<sign>\d*)')
m = p.match(js)
print u"match {}".format(m.group(1))
print "groupdict = \n\t{}".format(m.groupdict())
#get email
p = re.compile(ur'[a-zA-Z]\w{7,}@\w+\.\w+')
m = p.search(js)
print m.group(0)

#conflict re
print u'----------conflict ------------'
#r = u'''{{(?:     #注意, 字符串会受到缩进的影响而变化长度
#            (?P<escaped>{{)|
#            (?P<named>[a-z][a-zA-Z0-9]*)}}|
#            {(?P<braced>(?P=named))}}}|
#            (?P<invalid>)
#            )
#        '''
r = u'\
{{(?:\
(?P<escaped>{{)|\
(?P<named>[a-z]*)\
)}}\
'

#print len(r)
#for i in r:
#    print ord(i)
#print r
p = re.compile(r)
#s = u'{{{{{{var}}}{{{hellovar}}}'
#s = u'{{{{'
s = u'{{{{hello}}'
print p.findall(s)

s = u'{{{{}}'
print p.findall(s)

s = u'{{{{}}{{{{abc}}'
print p.findall(s)

#非贪婪模式
print u''
print u'--------非贪婪模式'
r = u'\d+?'
s = u'1234x'
p = re.compile(r)
m = p.match(s)
print m.group(0)


r = u'\d{2,4}?'
p = re.compile(r)
m = p.match(s)
print m.group(0)

#多行正则表达式(主要使用来测测换行与tab对正则有没有影响)
r = ur'''\d+_\w+(?:
_\d+)'''
s = u'123_abc_456'
p = re.compile(r)
m = p.match(s)
#print m.group(0)

print u'----------------'
r = r"""
    %(delim)s(?:
      (?P<escaped>%(delim)s) |
      (?P<named>%(id)s)      |
      {(?P<braced>%(id)s)}   |
      (?P<invalid>)
    )
    """ % ({u'delim':ur'\$', u'id' : ur'[_a-z][_a-z0-9]*'})
    #.replace(ur' ',u'').replace(u'\n',u'') % ({u'delim':ur'\$', u'id' : ur'[_a-z][_a-z0-9]*'})

r2 = '\
%(delim)s(?:\
(?P<escaped>%(delim)s)|\
(?P<named>%(id)s)|\
{(?P<braced>%(id)s)}|\
(?P<invalid>)\
)\
' % ({u'delim':ur'\$', u'id' : ur'[_a-z][_a-z0-9]*'})

#r = ur'%(delim)s(?:(?P<named>%(id)s))' % ({u'delim':u'\$', u'id' : ur'[_a-z][_a-z0-9]*'})
#r = ur'\$[_a-z][_a-z0-9]*'
#r = ur'(\$)|[_a-z]+'
print r
s = u' $$ is best'
p = re.compile(r, re.VERBOSE)
m = p.findall(s)
print m

m = p.sub(ur'roke \1 ', s)
print m



#嵌套的分组的序号的问题
print u'嵌套的分组的序号的问题------------------------'
print u'____________1__________'
import re

r = u'(\w+(123)\w+) (ok!!!)'
s = u'abc123defg ok!!! shabi'
p = re.compile(r)
m = p.search(s)
print u'm.groups() = {}'.format(m.groups())
for i in xrange(len(m.groups()) + 1):
    print u'm.group({}) = {} '.format(i, m.group(i))

#注意(?<=xxx)中 xxx需要是固定长度的模式
print u'____________2__________'
r = u'(?<=\w{3}(123))\w+ (ok!!!)'
s = s
p = re.compile(r)
m = p.search(s)
print u'm.groups() = {}'.format(m.groups())
for i in xrange(len(m.groups()) + 1):
    print u'm.group({}) = {} '.format(i, m.group(i))

    
