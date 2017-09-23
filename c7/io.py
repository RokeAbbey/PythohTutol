#coding=utf-8


#repr 
'''
    注意 print 在打印','分割的诸项时会自动添加空格分割,所以你运行后会发现两次结果不对齐
'''
'''
for i in xrange(1,11):
    print repr(i).rjust(2), repr(i*i).rjust(3),
    print repr(i**3).rjust(4)

for i in xrange(1,11):
    print '{0:2d}{1:3d}{2:4d}'.format(i, i*i, i**3)


for i in xrange(1,11):
    print repr(i).ljust(2), repr(i*i).ljust(3),
    print repr(i**3).ljust(4)

'''

#variable format methods
'''
    各种各样格式化字符串的方法
'''

'''
students = {'Roke':100, 'Lou':0, 'Fei': 60}
num = len(students)
keys = students.keys()
values = students.values()
print 'method 1:'
for i in range(0,num):
    print ('name : {0[%s]:5} scores : {1[%s]:5d}' % (i, i)).format(keys, values)

print 'method 2:'
roke = {'name' : 'Roke', 'scores' : 100}
lou = {'name': 'Lou', 'scores': 0}
fei = {'name': 'Fei', 'scores': 60}
students = (roke, lou, fei)
for stu in students:
    print 'name : {0[name]:5} scores : {0[scores]:5d}'.format(stu)
    
print 'method 3:'
for stu in students:
    print 'name : {name:>15} scores : {scores:15.3f}'.format(name=stu['name'], scores=stu['scores'])

'''

#open read write
print u'write text start'
with open('text1.dat','w') as f:
    for i in xrange(0,10):
        f.write(unicode(i)*i+'\n')
print u'write text end'

print u'read text start'
with open('text1.dat','r') as f:
    for line in f:
        print line,
        
    
print
print u'read text end'

print u'read text start again'
position = []
with open('text1.dat','r+') as f:
    for i in xrange(0,10):
        if i & 1 == 0:
            print '*' * i
        else:
            f.seek((1 + i ) * i / 2,0)
            position.append(f.tell())
            print f.readline(),

print u'read text finish'
print u'positions are :{}'.format(position)
