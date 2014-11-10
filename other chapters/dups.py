def dups(x):
    a=[]
    for c in x:
        y=x.count(c)
        if y>1:
            x.remove(c)
            a.append(c)
    return a