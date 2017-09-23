# coding=utf-8

u"""
    'c'----1    1
    'b'----1    1
    'B'----1    1
    'u'----2    4
    'h'----2    2
    'H'----2    2
    'i'----2    4
    'I'----2    4
    'l'----4    8
    'L'----4    8
    'f'----4    4
    'd'----8    8
"""
"""
from array import array

a = array(u'i', [1, 2, 4, 3])
print a.itemsize
info = a.buffer_info()
print info  #(address, length) = (xxxx, 4)
print u'the ocupation in memory of this array is {}'.format(info[1] * a.itemsize)

s = u'cbBuhHiIlLfd'
print list((array(i).itemsize for i in s))

#byteswap
a = array(u'c', 'abcdefg')
a.byteswap()
print a

a = array(u'h',[123, 456])
a.byteswap()
print a
'''
    123:0000 0000 0111 1011             0111 1011 0000 0000 ---> 31488
    456:0000 0001 1100 1000             1100 1000 0000 0001 ---> 51201  --->  -14335
'''

a = array(u'u', u'abcdefhelloworld')
a.byteswap()
print a
a.byteswap()
print a.count(u'o')

"""


#exaple of fromlist, fromfile
print u'---------------------------'

from array import array


a = array(u'i')
a.fromlist(list(xrange(5)))
print a

# a.fromlist(list((str(x) for x in xrange(5))))     #TypeError happened
# print a                   

with open(u'file1.dat', u'w') as f:
    f.writelines((str(x) for x in xrange(4)))

with open(u'file1.dat', u'r') as f:
    for line in f.readlines():
        print line

a.fromfile(file(u'file1.dat', u'r'), 1)  
'''
        由于a的typecode 是i, 所以每个item占用4个字节,所以文件中的文本所占的字节数必须是4的倍数, 所以
    下面*1处的xrange中的参数选为4
        但是写出去的是str, 其实写的是编码值 也就是48 49 50 51
        但是读进来的时候是小端读入,并且将这4个字节视作一个int, 因此 是 (51 << 24) + (50 << 16) + (49 << 8) + 48 =  858927408
'''
print a
b = 0
for x in (ord(str(i)) for i in xrange(4)):# *1
    # print x
    b = (b << 8) + x

print b

a.byteswap() #注意看 最后一项是等于b的 808530483 说明读入的时候是小端读入
print a

#858927408 --> 0011 0011 0011 0010 0011 0001 0011 0000 == 33323130H

# from unicode, fromstring
print u'-------------------------------'
a = array(u'u')
a.fromunicode(u'abcdefg')
print a

a.fromstring('hijkmnlo')
print a
# a.fromlist([123 << 24, 456 << 22, 789 << 21, 10 << 24])  #会报错,虽然上面那个fromstring成功
# print a



a = array(u'c')
a.fromstring('abcdefg')
print a
# a.fromunicode(u'hijkmnlo')    #报错,虽然上面那个fromstring成功
# print a

# to

# example of index insert pop remove reverse
print u'-------------------------'
a = array(u'i')
a.fromlist(list(x for x in xrange(5, 10)))
for i in xrange(len(a)):
    print u'a.index({}) is {} '.format(i, a[i])

a.insert(2, -2)
print u'a = {}'.format(a)

a.pop(2)
print u'a = {}'.format(a)

a.remove(9)
print u'a = {}'.format(a)

a.reverse()
print u'a = {}'.format(a)

# example of toList toString toUnicode toFile
print u'--------------------------'

a = array(u'u',u'你好')
print u'a.tolist() = {}'.format(a.tolist())

print u'a.tostring() = {} '.format(a.tostring())
with open(u'file2.dat', u'w') as f:
    a.tofile(f)  
    '''
        写出去是当做str来写的
        你好 == \u4f60\u597d ----> chr(f6) chr(60) chr(59) chr(7d) --->\u00f6\u0060\u0059\u007d
        所以下面用普通方法读进来的就是乱码,而且无论怎么encode decode都没办法

        而下面用fromfile读进来的 成了 "你好你好"我也不知道他怎么读的 
    '''
with open(u'file2.dat', u'r') as f:
    print u'a.tofile() and the contents are: '
    for line in f:
        print line.encode(u'utf-8')# .decode(u'ascii').encode(u'utf-8')

#a = array(u'u')
a.fromfile(file(u'file2.dat', u'r'), 2)
print a
for i in a:
    print i
# a.byteswap()
# print a
# print u'a.fromfile() = {}'.format(, 2))
"""
import codecs
with codecs.open(u'file2.dat', mode=u'w', encoding=u'utf-8') as f:
    a.tofile(f)

# codecs中的file不是我们平常用的file , 所以会报错
"""
# 用struct来弥补上述错误
print u'--------------------------------'
import struct
with open(u'file2.dat', u'r') as f:
    data = ''.join(f.readlines())
    print data
    newdata = array(u'u')
    for x in xrange(len(data) >> 1):
        first, second = struct.unpack(u'bb', data[x << 1 : (x << 1) + 2])
        #注意 读进来的时候是按照str来读的, 所以\u00f6 --> 0xf6
        
        newdata.append(unichr((second << 8) + first))

    print newdata
    print u''.join(newdata)
    print u'len = {}'.format(len(u''.join(newdata)))


