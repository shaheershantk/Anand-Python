def head(x):
    f=open(x).readlines()
    for i in range(0,10):
        print f[i]
        
def tail(x):
    y=len(open(x).readlines())
    if y<10:
        return head(x)
    else:
        f=open(x).readlines()
        for i in range(y-10,y):
            print f[i]
        