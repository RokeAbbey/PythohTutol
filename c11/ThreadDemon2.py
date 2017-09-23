#coding=utf-8

#example of condition_2

'''
import threading, time
import random
class Buffer(object):
    def __init__(self):
        self.__buf = []
        self.__con = threading.Condition()

    def bufIsEmpty(self):
        return len(self.__buf) == 0

    def release(self):
        self.__con.release()

    def acquire(self):
        self.__con.acquire()

    def notify(self, num=1):
        self.__con.notify(num)

    def notifyAll(self):
        self.__con.notifyAll()

    def putProduct(self, pro):
        self.__buf.append(pro)
    
    def getProduct(self):
        return self.__buf.pop(0)

    def printBuf(self):
        print self.__buf

    def wait(self, num=None):
        self.__con.wait(num)

class Producer(threading.Thread):
    def __init__(self, buf, name):
        super(Producer, self).__init__(name=name)
        self.__buf = buf

    def run(self):
        #print u'{} start'.format(self.getName())
        for i in xrange(5):
            self.producer()
            time.sleep(5)

    def producer(self):
        #print u'{} before acquire'.format(self.getName())
        self.__buf.acquire()
        #print u'{} after acquire'.format(self.getName())
        print u'{} produce'.format(self.getName())
        self.__buf.putProduct(u'{} make this product'.format(self.getName()))
        self.__buf.notify()
        #print u'{} before release'.format(self.getName())
        self.__buf.release()
        #print u'{} after release'.format(self.getName())

class Consumer(threading.Thread):
    def __init__(self, buf, name):
        super(Consumer, self).__init__(name=name)
        self.__buf = buf

    def run(self):
        #print u'{} start'.format(self.getName())
        #print u'{} before acquire'.format(self.getName())
        self.__buf.acquire()
        #print u'{} after acquire'.format(self.getName())
        for i in xrange(5):
            self.consume()
        #print u'{} before release'.format(self.getName())
        self.__buf.release()
        #print u'{} after release'.format(self.getName())

    def consume(self):
        #print u'{} empty : {}'.format(self.getName(), self.__buf.bufIsEmpty())
        while self.__buf.bufIsEmpty():
            self.__buf.wait()

        pro = self.__buf.getProduct()
        print u'{}: get -- {}'.format(self.getName(), pro)
        #self.__buf.printBuf()
buf = Buffer()
ps = (Producer(buf, u'p'+str(i)) for i in xrange(3))
cs = (Consumer(buf, u'c'+str(i)) for i in xrange(3))
for p in ps:
    p.start()

for c in cs:
    c.start()
'''

#example of semaphore

'''
import threading, time
class Buffer(object):
    def __init__(self, limitedSize, emptySize=None):
        super(Buffer, self).__init__()
        self.__limitedSize = limitedSize
        self.__emptySize = emptySize if emptySize or emptySize == 0 else limitedSize
        self.__buf = [u'init product {}'.format(i) for i in xrange(limitedSize - self.__emptySize)]
        self.__prods = threading.Semaphore(1)
        self.__empty = threading.Semaphore(1)

    def putProduct(self, pro):
        self.__empty.acquire()
        print u'{} put '.format(threading.currentThread().getName())
        flag = self.empty()
        self.__buf.append(pro)
        if not self.full():self.__empty.release()
        if flag : self.__prods.release()

    def getProduct(self):
        self.__prods.acquire()
        #print u'{} get '.format(threading.currentThread().getName())
        flag = self.full()
        pro = self.__buf.pop(0)
        if not self.empty():self.__prods.release()
        if flag : self.__empty.release()
        return pro

    def empty(self):
        return len(self.__buf) == 0

    def full(self):
        return len(self.__buf) == self.__limitedSize

    def showBuf(self):
        print self.__buf
        return self
class Producer(threading.Thread):
    def __init__(self, name, buf):
        self.__buf = buf
        super(Producer, self).__init__(name=name)

    def run(self):
        for i in xrange(5):
            #print u'{} product'.format(self.getName())
            self.__buf.putProduct(u'product {} made by {}'.format(i, self.getName()))
            time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, name, buf):
        self.__buf = buf
        super(Consumer, self).__init__(name=name)

    def run(self):
        for i in xrange(5):
            pro = self.__buf.getProduct()
            print u'{} :get --- {} '.format(self.getName(), pro)
            self.__buf.showBuf()

buf = Buffer(limitedSize=4, emptySize=2)
list((Producer(u'p'+str(i), buf).start() for i in xrange(5)))
list((Consumer(u'c'+str(i), buf).start() for i in xrange(5)))
#buf.showBuf()
'''


# example of timer
import threading
import time
import pprint


def getTarget():
    i = 0

    def target():
        print i 
        # i = i + 1 #闭包bug
        # tm.start() #只能被start 1 次
    return target


tm = threading.Timer(1, getTarget())
pp = pprint.PrettyPrinter(width=80, indent=4)
pp.pprint(dir(getTarget()))

print u'------------'
pp.pprint(getTarget().func_dict)

print u'------------'
pp.pprint(getTarget().func_closure)
help(getTarget().func_closure)
print u'------------'
pp.pprint(getTarget().func_name)

print u'------------'
pp.pprint(getTarget().func_globals)

print u'------------'
pp.pprint(getTarget().func_defaults)

tm.start()

time.sleep(10)

tm.cancel()






