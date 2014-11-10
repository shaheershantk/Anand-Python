def enumerate(lists):
    a=iter(lists)
    return [(a.next(),i) for i in range(len(lists))]
    
print enumerate([1,2,3])