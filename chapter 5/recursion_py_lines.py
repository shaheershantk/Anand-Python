import os
count=0
    
def fun(dir):
    a=os.listdir(dir)
    
    for c in a:
        path=os.path.join(dir,c)
        if os.path.isdir(path)==True:
             fun(path)
        elif(c.split('.')[-1]=='py'):
            print c
            os.chdir(dir)
            global count
            count+= len(open(c).readlines())
            
    return count