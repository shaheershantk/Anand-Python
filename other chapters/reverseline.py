f=open('x.txt').readlines()
x= len(f)
b=''
for i in range(0,x):
    b=f[i]
    f[i]=b[::1]
    
b=open('x.txt','w')
b.writelines(f[::-1])
b.close()
