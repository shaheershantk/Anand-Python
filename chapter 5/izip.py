def izip(a,b):
    c=iter(a)
    d=iter(b)
    return [(c.next(),d.next()) for i in range(len(a))]
    
print izip(['a','v','c'],[1,2,3])