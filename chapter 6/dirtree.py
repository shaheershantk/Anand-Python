k=0
n=0
def dirtree(dir1):
    import os
    a=os.listdir(dir1)
    global k,n
    if k==0:
        n=len(dir1.split('/'))
    print dir1.split('/')[-1]+'/'
    k+=1
    for c in a:
        if os.path.isdir(c):
            i=len(dir1.split('/'))-n
            for j in range(i):
                print '|  ',
            if c==a[-1]:
                print '\__',dirtree(os.path.join(dir1,c))
            else:
                print '|__',dirtree(os.path.join(dir1,c))
        else:
            i=len(dir1.split('/'))-n
            for j in range(i):
                print '|  ',
            if c==a[-1]:
                print '\__',c
            else:
                print '|__',c
    return dir1.split('/')[-1]+'/'
            
                        



dirtree('/home/vvv')