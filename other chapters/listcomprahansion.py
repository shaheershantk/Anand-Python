a=[1,2,3]
b=["a", "b", "c"]
print [(x,y) for x in a for y in b[x-1]]