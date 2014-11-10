def grep(file,word):
    f=open(file).readlines()
    for i in range(0,len(f)):
        if word in f[i]:
            print f[i]
        
