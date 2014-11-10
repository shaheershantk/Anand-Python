def group(x,y):
    n=len(x)/y
    a=0
    b=[]
    d=[]
    for i in range(0,n):
        c=x[a:a+y]
        a=a+y
        b.append(c)
    if len(x)%y!=0:
        d=x[n*y:]
        print b+[d]
    else:
        print b