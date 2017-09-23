#coding=utf-8
import getopt
import sys
if __name__ == u'__main__':
    opt, args = getopt.getopt(sys.argv[1:], u'help:', [u'help', u'version', u'output=', u'input='])
    print u'opt = {}, args = {}'.format(opt, args)
    for o, a in opt:
        if o == u'-h' or o == u'--help':
            print u'show the help docs'

        elif o == u'-e':
            print u'show the error logs'

        elif o == u'-l':
            print u'the o is l'

        elif o == u'-p':
            print u'the o is p, and a is {}'.format(a)

        elif o == u'--version':
            print u'show the version details'

        elif o == u'--output':
            print u'o is output, and a is {}'.format(a)

        elif o == u'--input':
            print u'o is input, and a is {}'.format(a)
