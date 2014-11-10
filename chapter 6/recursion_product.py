def mul(x,n):
    if n==0:
        return 0
    else:
        return x+mul(x,n-1)