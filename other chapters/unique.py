def unique(x):
    for c in x:
        y=x.count(c)
        if y>1:
            x.remove(c)
    return x