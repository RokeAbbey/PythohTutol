#coding=utf-8
#json
import json
numeralList = range(0,10)
students = ({'name':'roke', 'scores':100},
            {'name':'lou', 'scores':0},
            {'name':'fei', 'scores':60}
           )

'''
js1 = json.dumps(numeralList)
print js1
'''
'''
js1 = json.dumps(students)
print u'type of js1 is {}'.format(type(js1))
print unicode(js1)

students2 = json.loads(js1)
print u'type of students2 is {}'.format(type(students2))
print students2
'''


from Student import Student
import json
students = [Student('roke',100),
           Student('lou',0),
           Student('fei',60)]

js1 = json.dumps(students, default=Student.student2dict)
print 'type of js1 is {}'.format(js1)
print 'js1 : {}'.format(js1)

students2 = json.loads(js1)
print u'type of students2 is {}'.format(students2)
print u'students2 : {}'.format(students2)
