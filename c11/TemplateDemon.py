#coding=utf-8
import re
from string import Template
files = [u'img001.jpg', u'img002.jpg', u'img003.jpg']
p = re.compile(u'img(.*)')
slist = []
for s in files:
    m = p.match(s)
    slist.append(m.group(1))
    #print u'm.group(1) = {}, type = {}'.format(m.group(1), type(m.group(1)))

#print slist
prefix = raw_input(u'input the prefix of the new Name:\t')
mubanstr = prefix + u'_n _hel'
print mubanstr

class MyTemplate(Template):
    delimiter = u'_'
newFiles = []
mt = MyTemplate(mubanstr)
for i in slist:
    newFiles.append(mt.safe_substitute(n=i))



print newFiles
print mt.substitute(n=u'i', hel=u'helllo')
print mt.pattern.pattern
print u'____________________________'
import pprint
pp = pprint.PrettyPrinter(width=1)#(width=20, indent=4, depth=4)
pp.pprint(dict(Template.__dict__))
#pprint.pprint(Template.__dict__, width=80, indent=4)
#myDict = {u'name':u'roke', u'grades':100}
#pp.pprint(myDict)

print u'____________________________'
class MyTemplate2(Template):
    delimiter = u'[['

    pattern = u''' '''
