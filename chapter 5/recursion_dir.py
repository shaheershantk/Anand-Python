import os
count=0
    
def fun(dir):
    a=os.listdir(dir)
    
    for c in a:
        path=os.path.join(dir,c)
        if os.path.isdir(path)==True:
             fun(path)
        elif(c.split('.')[-1]=='js'):
            global count
            count+=1
    return count