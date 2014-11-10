a=['a','s','d']
def enumerate(a):
    return [(x,y) for x in range(len(a)) for y in a[x] ]