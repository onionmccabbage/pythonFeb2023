import doctest

def sq(n):
    '''
    >>> sq(3)
    12
    '''
    return n*n

if __name__ == '__main__':
    # print(sq(3)) # 9
    doctest.testmod(verbose=True)