#coding=utf-8

#generator
'''
def abc():
    print u'enter into abc'
    for i in xrange(0, 10):
        n1 = i
        print u' before yield : n1 = {}'.format(n1)

        n1 = yield i
        print u' after yield : n1 = {}'.format(n1)

    print u'away from abc'

gen = abc()
result = gen.send(None)
for i in xrange(10, 0, -1):
    print u'result = {}'.format(result)
    result = gen.send(i)


print u'result = {}'.format(result)
'''

#generator expression
real = (1, 2, 3)
imagine = (1, 2, 3)
gen = (complex(x, y) for x, y in zip(real, imagine))
while True:
    print gen.next()

