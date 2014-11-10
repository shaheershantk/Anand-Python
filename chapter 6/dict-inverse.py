import copy
dict2={}
def unflat(dict1):
    b=[]
    dict3={}
    for c in dict1:
        a=c.split('.')
        if (a==[c]):
            dict2[c]=dict1[c]
        else:
            if b==a[0]:
                b=a[0]
                dict3[a[-1]]=dict1[c]
                x='.'.join(a[:-1])
                dict2[x]=dict3
            else:
                b=a[0]
                dict3={}
                dict3[a[-1]]=dict1[c]
                dict2['.'.join(a[:-1])]=dict3
    print dict2      
    dict4=copy.copy(dict2)
    for key in dict2:
        if len(key.split('.'))==1:
           pass
        else:
            unflat(dict4) 
    return dict2
