def uniquestr(x):
    z=[]
    for c in x:
        z.append(c.lower())
    y=[]
    y[:]=z
    for c in z:
        y.remove(c)
        if c in y:
           z.remove(c)
    return z
        
        