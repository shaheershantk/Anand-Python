import os
a=raw_input('path=')
x=os.listdir(a)
for c in x:
    y=os.stat(a+'/'+c)
    print c,
    print y[7],
    print y[9]