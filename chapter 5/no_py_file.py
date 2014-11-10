import os
def find_no(direc):
    a=os.listdir(direc)
    count=0
    for i in range(len(a)):
        if a[i].split('.')[-1]=='py':
           count+=1
    return count
    
    
print find_no('/home/vvv')