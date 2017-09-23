#coding=utf-8
import struct
import pprint
import repr
#example from document 11
'''
with open(u'test.zip',u'rb') as f: #待会换成r试试看
    data = f.read()
    print type(data)
    start = 0
    for i in range(3):
        start += 14
        fields = struct.unpack(u'<IIIHH',data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
        fields = {
            u'crc32'   :   crc32,
            u'comp_size'    :    comp_size,
            u'uncomp_size'    :    uncomp_size,
            u'filenamesize'    :    filenamesize,
            u'extra_size'    :    extra_size
        }
        pp = pprint.PrettyPrinter(width=80, depth=3, indent=4)
        pp.pprint(fields)

        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        
        content = {
            u'filename'    :    filename,
            u'hex(crc32)'    :    hex(crc32),
            u'comp_size'    :    comp_size,
            u'uncomp_size'    :    uncomp_size,
            u'extra'    :    repr.repr(extra)
        }
        pp.pprint(content)
        start += extra_size + comp_size
'''

# example
print u'-------------------------'
info = u'hello, -world!!!'
fields = struct.unpack(u'<IIII', info)
print fields

for i in range(4):
    s = 0  # 大端
    s2 = 0  # 小端
    for j in range(4):
        # print (i,j)
        # print info[i * 4 + j]
        s = (s << 8) + ord(info[i * 4 + j]) 
        s2 += ord(info[i * 4 + j]) << j * 8
    print s
    print s2
    
print (ord(u'h') << 24 ) + (ord(u'e') << 16) + (ord(u'l') << 8) + (ord(u'l'))
print (ord(u'h') << 0 ) + (ord(u'e') << 8) + (ord(u'l') << 16) + (ord(u'l') << 24)

# example struct.pack 为什么cI是8个字节


import struct


print u'------------------'

s = u'abcdefgh'
print u'struct.calcsize({}) = {}'.format(u'cI', struct.calcsize(u'cI'))
a = struct.unpack(u'ccccI', s)      # 如果改成cI也是八个字节
print len(a)
print a
# print u'pre = {}'.format(pre)
a = a[4]
print u'a = {}'.format(a)

b = a
t = 0
while True:
    m = b & 0xff
    print u'b & 0xff == {} , chr == {}'.format(m, chr(m))
    b = b >> 8
    print u'b = {}'.format(b)
    t += 1
    if b == 0 or t >= 20:
        break

