import os
count=0
    
def fun(dir):
    a=os.listdir(dir)
    j=0
    for c in a:
        path=os.path.join(dir,c)
        if os.path.isdir(path)==True:
             fun(path)
        elif(c.split('.')[-1]=='txt'):
            print c
            os.chdir(dir)
            global count
            a=open(c).readlines()
            for line in a:
                if (line=='\n') or '#' in list(line):
                    pass
                else:
                    j+=1
            count =count+j
                    
                
    return count