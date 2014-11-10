def extsortx(x):
    y=[]
    b=''
    p=''
    for i in range(0,len(x)):
        ai=x[i].split('.')
        y.append(ai[1])
    for c in x:
        for i in range(0,len(x)-1):
            if y[i]>y[i+1]:
                p=y[i]
                y[i]=y[i+1]
                y[i+1]=p
                b=x[i]
                x[i]=x[i+1]
                x[i+1]=b
        
                
    return x