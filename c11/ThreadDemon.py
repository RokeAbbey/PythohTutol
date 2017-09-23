#coding=utf-8

#example of threading_1 and zipfile
"""
import zipfile, threading
class AsyncZip(threading.Thread):
    def __init__(self, inputName, outputName):
        self.__inputName = inputName
        self.__outputName = outputName
        super(AsyncZip, self).__init__()
        
    def run(self):
        f = zipfile.ZipFile(self.__outputName, u'w', zipfile.ZIP_DEFLATED)
        f.write(self.__inputName)
        f.close()
        print u'the compression finish'

az = AsyncZip(u'json', u'jsonzip.zip')
az.start()
print u'compression start!!'
az.join()
print u'mainthread wait for az'
"""

#example of threading_2
#practice of the methods in threading module
"""
import threading, time

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        time.sleep(1)
        print u'still alive  hahahaha'

print u'1. the alive threads count = {}'.format(threading.activeCount())

threads = list(MyThread() for i in range(10))
for t in threads:
    #t.setDaemon(True) #note_1: if you remove the '#' front of the t.setDaemon, you can see 'still alive ...'
    t.start()
    print u'thread.isDaemon = {}'.format(t.isDaemon())
    #print u'2. the alive threads count = {}'.format(threading.activeCount())


print u'3. the alive threads count = {}'.format(threading.activeCount())
print u'1. the len(threading.enumerate()) = {}'.format(len(threading.enumerate()))
for t in threads:
    t.join()
#threads[0].join()
print u'4. the alive threads count = {}'.format(threading.activeCount())
print u'2. the len(threading.enumerate()) = {}'.format(len(threading.enumerate()))

print u'currentThread : {}'.format(threading.currentThread())

#请注意,generator是只能迭代一次的
"""
"""
a = (x for x in xrange(10))
print a
for i in a:
    print i

for i in a:
    print i
"""

#example threading.Event
"""
import threading, time
class MyThread(threading.Thread):

    def __init__(self, event, name=None):
        super(MyThread, self).__init__(name=name)
        self.event = event

    def run(self):
        while not self.event.isSet():
            print u'waiting for ......'
            self.event.wait(1)

        print u'finish waiting'
evt = threading.Event()
mt = MyThread(evt, u't1')
mt2 = MyThread(evt, u't2')

mt.start()
mt2.start()
time.sleep(3)
evt.set()
"""

#example with threading.Lock
'''
import threading
import time
u"""
    lock.acquire(False) 会返回一个bool值, 这个bool指表示当前的acquire操作有没有施加锁
    若A线程进入临界区且施加锁, 那么此时B线程调用lock.acquire(False)时候会返回false,并且不会阻塞, 因为虽然临界区有锁,但是却不是B线程施加的
    若B线程进入临界区,且临界区没有施加锁, 那么上述方法(以及参数)会施加一个锁, 此时返回True
"""
def target(lock, name):
    flag = True
    print u'{}: before enter '.format(name) 
    flag = lock.acquire(False)
    print u'{}: the return of lock.acquire is {}' .format(name, flag)
    print u'{}: entered into '.format(name)
    time.sleep(1)
    if flag : lock.release()
    print u'{}: release '.format(name)


lock = threading.Lock()
t1 = threading.Thread(target=target, name=u't1', args=(lock, u't1'))
t2 = threading.Thread(target=target, name=u't2', args=(lock, u't2'))
t1.start()
t2.start()
print u'{}: before enter '.format(u'main')
print u'{}: the return of lock.acquire is {}' .format(u'main', lock.acquire(True))
print u'{}: entered into '.format(u'main')
time.sleep(8)
lock.release()
print u'main out'
'''

#example with threading.rlock

'''
import threading
import time
def target(lock, name, flag=True):
    print u'{} is started'.format(name)
    lock.acquire(flag)
    lock.acquire(flag)
    print u'{} entered into '.format(name)
    time.sleep(1 if name != u't4'else 4)
    if not flag : 
        lock.release()#t4会报错,因为t4 acquire之后拿不到锁,但是他是false 所以可以直接通过, 但也因此不能release, 因为不能release非自己获得的锁(Rlock好像是不能被别人release的, lock可以 下个例子试试)
        print u'{} release'.format(name)
    time.sleep(1 if name != u't4'else 4)
    if not flag : 
        lock.release()
        print u'{} release'.format(name)
    print u'{} leave from '.format(name)

lock = threading.Lock()
rlock = threading.RLock()
t1 = threading.Thread(target=target, name=u't1', args=(lock, u't1', True))
t2 = threading.Thread(target=target, name=u't2', args=(lock, u't2', False))

t3 = threading.Thread(target=target, name=u't3', args=(rlock, u't3', True))
t4 = threading.Thread(target=target, name=u't4', args=(rlock, u't4', False))

t1.start();t2.start();t3.start();t4.start()

time.sleep(5)
'''

#example to comfirm wether the lock and rlock can be release by other thread witch not own the lock

"""
import threading
import thread
import sys
import traceback
import time
import re
def getClassName_prepare(depth=1):
    p = re.compile(u'(?:(?<=<class)|(?<=<type)) \'(?:\\w+\\.)*((?:\\w+\\.){'+str(depth - 1)+'}[\\w]+)\'')
    '''
    print p.pattern
    s = u"<type 'thread.lock'>" #u'<class \'_abc._efg\''#u'<type \'abc\''
    m = p.search(s)
    print m
    for i in xrange(len(m.groups()) + 1):
        print u'group({}) = {}'.format(i, m.group(i))
    print u'groups() = {}'.format(m.groups())
    '''
    def a(s):
        #print s
        return p.search(s).group(1)

    return a 

getClassName = getClassName_prepare()
def target1(lock, name):
    print u'{} start!!'.format(name)
    class_name = getClassName(str(lock.__class__))+u'__owner'
    print u'{} getident() = {} rlock.getowner = {}'.format(name, thread.get_ident(), 
                                                              getattr(lock, class_name) if hasattr(lock, class_name) else None)
    lock.acquire()
    print u'{} getident() = {} rlock.getowner = {}'.format(name, thread.get_ident(), 
                                                              getattr(lock, class_name) if hasattr(lock, class_name) else None)
    print u'{} leave without release'.format(name)

def target2(lock, name, flag):
    print u'{} start!!'.format(name)
    print u'{} enter into without acquire'.format(name)
    try:
        class_name = getClassName(str(lock.__class__))+u'__owner'
        print u'{} getident() = {} rlock.getowner = {}'.format(name, thread.get_ident(), 
                                                              getattr(lock, class_name) if hasattr(lock, class_name) else None)
        lock.acquire(flag)

        print u'{} getident() = {} rlock.getowner = {}'.format(name, thread.get_ident(), 
                                                              getattr(lock, class_name) if hasattr(lock, class_name) else None)
        lock.release()
        print u'{} leave'.format(name)

    except RuntimeError as re:
        print u'some error happened in {}  ____ '.format(name)
        exc_name, exc_value, exc_tb = sys.exc_info()
        traceback.print_exception(exc_name, exc_value, exc_tb)

lc = threading.Lock()
rlc = threading.RLock()
t1 = threading.Thread(target=target1, name=u't1', args=(lc, u't1'))
t2 = threading.Thread(target=target2, name=u't2', args=(lc, u't2', False))

t3 = threading.Thread(target=target1, name=u't3', args=(rlc, u't3'))
t4 = threading.Thread(target=target2, name=u't4', args=(rlc, u't4', False))

t1.start(); t3.start()
time.sleep(1)
t2.start();
#time.sleep(2)
t4.start()
"""

#example of condition
#下述代码执行失败,因为Condition的锁也是只能持有者进行Notify.

import threading, time

#enough = threading.Condition()


'''
class Buffer(object):
    def __init__(self, limitedSize):
        self.__buf = []
        self.__limitedSize = limitedSize
        self.__enough = threading.Condition()
        self.__empty = threading.Condition()

    def setLimitedSize(self, newSize):
        self.__limitedSize = limitedSize
        return self

    def getLimitedSize(self):
        return self.__limitedSize

    def putProduct(self, pro):
        if self.bufIsNotFull():
            self.__buf.append(pro)
        else:
            raise BufferSizeOverError(u'buf is full')
    
    def bufIsNotFull(self):
        return len(self.__buf) < self.__limitedSize

    def getEnoughCon(self):
        return self.__enough

    def bufIsNotEmpty(self):
        return len(self.__buf) > 0

    def getEmptyCon(self):
        return self.__empty

    def getProduct(self):
        return self.__buf.pop(0)

    class BufferSizeOverError(Exception):
        def __init__(self, msg):
            super(BufferSizeOverError, self).__init__(self, msg)

class Consumer(threading.Thread):
    def __init__(self, name, buf):
        super(Consumer, self).__init__(name=name)
        self.__buf = buf

    def run(self):
        print u'{} before acquire'.format(self.getName())
        self.__buf.getEmptyCon().acquire()
        print u'{} after acquire'.format(self.getName())
        for i in xrange(5):
            self.consume()
            time.sleep(1)
        self.__buf.getEmptyCon().release()

    def consume(self):
        while not self.__buf.bufIsNotEmpty():
            self.__buf.getEmptyCon().wait()
        p = self.__buf.getProduct()
        self.__buf.getEnoughCon().notify()
        print u'{} consume the product : {}'.format(self.getName(), p)

class Producter(threading.Thread):
    def __init__(self, name, buf):
        super(Producter, self).__init__(name=name)
        #self.__con = con
        self.__buf = buf

    def run(self):
        print u'{} before acquire'.format(self.getName())
        self.__buf.getEnoughCon().acquire()
        print u'{} after acquire'.format(self.getName())
        for i in xrange(5):
            self.produce()
            time.sleep(1)
        self.__buf.getEnoughCon().release()


    def produce(self):

        while not self.__buf.bufIsNotFull():
            self.__buf.getEnoughCon().wait()

        self.__buf.putProduct(u'product from {}'.format(self.getName()))
        self.__buf.getEmptyCon().notify()

buf = Buffer(2)
consumers = (Consumer(name=u'c'+str(i), buf=buf) for i in xrange(3))
producters = (Producter(name=u'p'+str(i), buf=buf) for i in xrange(3))

for c in consumers:
    c.start()

for p in producters:
    p.start()

'''






