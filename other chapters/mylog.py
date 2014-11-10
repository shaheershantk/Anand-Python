def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    y=0
    for n in range(0,x):
        if b**n > x:
            return y
        elif b**n <=x:
            y=n
