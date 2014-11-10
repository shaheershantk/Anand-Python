def lists(x):
    import os
    y=os.listdir(x)
    for c in y:
        try:
            print '|__'+ c,
            print listss(c)
        except:
            pass
def listss(c):
     import os
     y=os.listdir(c)
     for val in y:
         try:
             if val==y[len(y)-1]:
                return '\__'+val
             else: 
                return '|  ' + val
         except:
            pass