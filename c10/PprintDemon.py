#coding=utf-8
import pprint
pp = pprint.PrettyPrinter(indent=10, width=10, depth=2)

loulou = {
    u'name':u'loulou',
    u'age':18,
    u'length':18,
    u'diameter':8,
    u'wifes':[]
}

loulou[u'wifes'] = [loulou]
roke = {
    u"name":u"Roke",
    u'age':18,
    u'length':18,
    u'diameter':8,
    u'wifes':[loulou]
    }

pp.pprint(roke)
print pp.isreadable(roke)
print pp.isrecursive(roke)
