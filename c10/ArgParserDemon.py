#coding=utf-8
#argparse
import argparse
import sys
'''
if __name__ == u'__main__':
    parse = argparse.ArgumentParser(prog=u'Argument Parser Test',
                                   #usage=u'Just a simple practice',
                                   description=u'description : nothing more than usage',
                                   epilog=u'epilog : epilog',
                                   prefix_chars=u'-+')
    parse.add_argument(u'integers', nargs=u'+', #action=u'store_const', const=sum, default=max,
                      type=int)
    parse.add_argument(u'--sum', u'-s', metavar=u'-s', action=u'store_const', const=sum, default=max, dest=u'func')
    
    parse.add_argument(u'--int', u'-i', action=u'store_const', const=int, dest=u'type')
    parse.add_argument(u'--float', u'-f', action=u'store_const', const=float, dest=u'type')
    parse.add_argument(u'floats', nargs=u'+', type=float)
    parse.add_argument(u'--str', type=unicode, dest=u'string', action=u'store', nargs=u'+')
    args = parse.parse_args()

    print args
    print args.func(args.integers)
    print args.func(args.floats)
    
    
'''
'''ArgParserDemon.py  1 2 3 4  1.1 1.2 -s -i -f 会报错,因为1.1被当成int, 没办法因为int的数量是+
    但是把1.2去掉的话就不会报错,因为1.1会被当做float'''
#nargs
if __name__ ==  u'__main__':
    parser = argparse.ArgumentParser(description=u'This is just a Demon of argparse about nargs')
    parser.add_argument(u'numbers', type=int, nargs=u'*', help=u'input the integers to get sum')
    parser.add_argument(u'--input', u'-in', nargs=u'?',
                        help=u'the data source file, default is stdin',
                        type=argparse.FileType(u'r'),
                        action=u'store',
                        default=sys.stdin,
                        dest=u'input1'
                       )
    parser.add_argument(u'--output', u'-out', nargs=u'?',
                        help=u'the result output file, default is stdout',
                        type=argparse.FileType(u'w'),
                        action=u'store',
                        default=sys.stdout
                       )
    parser.add_argument(u'--sum', u'-s',
                        help=u'if present, will sum the input numbers, otherwise will get the max of input numbers',
                        action=u'store_const',
                        const=sum,
                        default=max
                       )
    parser.add_argument(u'others', nargs=argparse.REMAINDER)#一般最好不要用remainder 因为会很烦,你会发现output等参数都算作others里面了,变得不正常, 把helloworld 之后的参数全部去掉之后又会正常的

    ''' + 起码要有一个参数 * 可以没有参数, ? 可以0-1个参数 当nargs=?时,若不显示标明--output, 则default生效,若标明--output 但其后不跟参数 则const生效,若标明--output 且跟参数,则后面的参数生效'''
    args = parser.parse_args(u' 1 2 3 --sum --input input.dat --output output.dat  helloworld how are you'.split())
    #args = parser.parse_args()
    print args
    args.numbers = args.numbers if args.numbers and len(args.numbers) > 0 else [10, 9, 8]
    print args.sum(args.numbers)
