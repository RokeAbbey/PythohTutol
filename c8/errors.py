#coding=utf-8
import sys
import traceback
f = lambda a,b: a/b
try:
    #print sys.argv
    print f(float(sys.argv[1]), float(sys.argv[2]))
    
except Exception as e:
    '''
    info = sys.exc_info()
    print u'**************error*****************'
    for i in info:
        print i

    #print help(info[2].__class__)
    print u'**************************'
    print info[2].tb_frame
    print info[2].tb_lasti
    print info[2].tb_lineno
    print info[2].tb_next

    #print u'e.errno = {}, e.strerror = {}'.format(e.errno, e.strerror)
    print u'e.args = {}'.format(e.args)
    print u'e.message = {}'.format(e.message)
    #traceback.print_exc()
    #sys.exc_info()[2].print_exc()


    '''
    info = sys.exc_info()
    exc_type, exc_value, exc_tb = info
    #print_tb
    #traceback.print_tb(info[2])
    
    #print_exc
    '''
    with open('error.txt','w') as fi:
        traceback.print_exception(*info, file=fi)
    '''
    traceback.print_exception(*info)
else:
    print u'nothing happened'

finally:
    print u'in finally'

