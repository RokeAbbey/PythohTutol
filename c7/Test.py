#coding=utf-8

from Class import Class as cls
from Student import Student as stu#待会试试把这句话去掉
import json
if __name__ == u'__main__':
    myclass = cls(u'软件工程1401')
    students = [stu('roke',100),
               stu('lou',0),
               stu('fei',60)]
    myclass.addStudents(students) \
            .addStudent(stu('god',99))

    #print unicode(myclass)
    print myclass._name
    print type(myclass._name)
    str = u'myclass._name = {}'.format(myclass._name)
    #print unicode(str)
    #print type(unicode(str))

    #print str.decode('utf-8')
   #print type(str.decode)
    js = json.dumps(myclass, default=cls.class2dict, ensure_ascii=False)
    print type(js)
    #print unicode(js).encode('utf-8')
    print js.decode('utf-8')#.encode('gbk')
    
