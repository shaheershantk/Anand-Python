def arrey(x,y):
    return [[None for i in range(y)] for j in range(x)]
    
a=arrey(2,3)
a[0][0]=5
print a