#coding=utf-8
import doctest
def average(*lst):
    """Computes the arithmetic mean of all the input args
    >>> print average(1, 2, 3)
    2
    """
    return sum(lst) / len(lst)

def getMax(*lst):
    '''get the max num in the input 
    >>> print getMax(-4, 2, 10, 8, 9, 5, 6, 2)  == 10
    True
    '''

    return max(lst)

doctest.testmod()
#print average(1, 2, 3)

