def wrap(file_name,length):
    f=open(file_name).readlines()
    for i in range(0,len(f)):
        if len(f[i])>length:
            if f[i][length-1]==' ':
                print f[i][0:length]
                print f[i][length:]
        else:
            print f[i]