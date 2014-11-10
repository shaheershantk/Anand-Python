def center(x):
    f=open(x).readlines()
    m=0
    for i in range(0,len(f)):
        m=max(m,len(f[i]))
        print m
    for i in range(0,len(f)):
        if len(f[i])<m:
            k=(m-len(f[i]))/2
            for j in range(0,k/2):
                print ' ',
            print f[i]
            
        else:
           print f[i] 