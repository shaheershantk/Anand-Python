def files(names):
    for name in names:
        for line in open(name):
            if len(line)>=40:
                yield line
x=files(['filee.txt','x.txt'])