dict2={}
def dicts(dict1):
    for key in dict1:
        value=dict1[key]
        if type(value)==dict:
            d={}
            for key1 in value:
                a='.'.join([key,key1])
                d[a]=value[key1]
                dicts(d)
        else:
            keys=dict1[key]
            dict2[key]=keys
            
    return dict2
print dicts({'a': 1, 'b': {'x': {'s':1,'d':2}, 'y': 3}, 'c':4})