import os
direc=raw_input("dir_name= ")
a=os.listdir(direc)
freq={}
c=[]
for i in range(len(a)):
    c.append(a[i].split('.')[-1])
for x in c:
    freq[x] = freq.get(x,0) + 1   
print freq         