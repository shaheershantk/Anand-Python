f=open('x.txt').readlines()
b=f[::-1]
f=open('x.txt','w')
f.writelines(b)
f.close()
