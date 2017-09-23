#coding=utf-8
class A(object):
    def __init__(self):
        print u'__init__ of A'

class B(A):
    def __init__(self):
        print u'__init__ of B'

B()

