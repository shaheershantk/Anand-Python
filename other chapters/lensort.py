def lensort(x):
    for str in x:
        for i in range(0,len(x)-1):
            if len(x[i])>len(x[i+1]):
                a=x[i]
                x[i]=x[i+1]
                x[i+1]=a
                
    return x
                
                
            
        