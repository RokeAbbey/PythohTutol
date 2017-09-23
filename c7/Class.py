#coding=utf-8
from Student import Student as student
import json

class Class(object):

    def __init__(self, name, students=None):
        self._name = name
        self.students = students if students else []

    def addStudent(self, stu):
        if self.students == None:
            self.students = []
        self.students.append(stu)
    
    def addStudents(self, stus):
        if not stus:
            return self 
        else:
            self.students.extend(stus)
        
        return self

    def removeStudent(stu, showDetails=None):
        if isinstance(stu, int):
            self.students.pop(stu)
        elif isinstance(stu, student):
            self.students.remove(stu)
        
        if showDetails:
            print u'isinstance(stu,student) = {}'.format(isinstance(stu, student))


    @staticmethod
    def class2dict(cls):
        dict = {}
        dict['className'] = cls._name.encode('utf-8')
        dict['students'] = json.dumps(cls.students, default=student.student2dict)
        return dict

    def __str__(self):
        return u'classname : {},\n studentsNum : {}'.format(self._name, len(self.students))
    
    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return Class.ClassIter(self)

    class ClassIter(object):

        def __init__(self, outcls):
            self.outcls = outcls
            self.currentIndex = 0

        def next(self):
            self.currentIndex += 1
            if  self.currentIndex > len(self.outcls.students):
                raise StopIteration
            return self.outcls.students[self.currentIndex - 1]

