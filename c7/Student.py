#coding=utf-8
class Student(object):
    totalNum = 0
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        Student.totalNum += 1

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return u'name : {}, scores : {}'.format(self.name, self.scores)

    def student2dict(self):
        print 'involked !!'
        return self.__dict__

    @classmethod
    def getTotalNum(cls):
        return cls.totalNum

