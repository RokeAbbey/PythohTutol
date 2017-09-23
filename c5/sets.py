#coding=utf-8
'''
numbers = range(1,10)
numbers[len(numbers):] = range(5,15)
distinctNumbers = set(numbers)
print unicode(distinctNumbers)
print type(distinctNumbers)
'''

class Fruits(object):
    def __init__(self, typ):
        self.type = typ

    def __str__(self):
#        print 'str'
        return unicode(self.type)

    def __repr__(self):
#        print 'repr'
        return unicode(self.type)

    def __eq__(self, obj):
#        print 'eq'
        return self.type == obj.type
    
    def __ne__(self, obj):
#        print 'ne'
        return self.type != obj.type

    def __cmp__(self, obj):
#        print u'in fruits\' cmp'
        if self > obj:
            return 1
        elif self == obj:
            return 0
        else:
            return -1
    
    def __gt__(self, obj):
#       print 'gt'
        return self.type > obj.type
    
    def __hash__(self):
        return hash(self.__str__())

    
numbers = set(xrange(1,6))
numbers2 = set(xrange(4,9))

f1 = Fruits("oringe")
f2 = Fruits("apple")
f3 = Fruits("apple")
f4 = Fruits('strawberry')
f5 = Fruits('peach')
fruits = set((f1, f2, f3))
fruits2 = set((f4, f5))




#print 'fruits is %s, len is %s ' % (unicode(fruits), unicode(len(fruits)))
#difference

'''
diff = numbers.difference(numbers2)
print unicode(diff)

'''

#discard
'''
diff.discard(1)
print unicode(diff)
print u'f1 == f2 %s' % unicode(f1 == f2)
print u'f3 == f2 %s' % unicode(f3 == f2)

'''
'''
fruits.discard(f3)
print unicode(fruits)
'''

#fruit cmp ge gt le lt
'''
print cmp(f1,f2)
print cmp(f2,f3)
'''

#update & union
'''
print unicode(fruits.union(fruits2))
fruits.update(fruits2)
print unicode(fruits)
'''

#dict test
t1 = (f1, f2, f3)
it = iter(t1)
data = {}
num = 0
for i in it:
    num += 1
    data[i] = num 

print type(data)
for k, v in data.iteritems():
    print 'key = %s , value = %s , keyType = %s' % (k, v, type(k))

#ks = data.keys()
#print 'k[0] == k[2] : %s' % (ks[0] == ks[2])
