class new:
    def __init__(self,a):
        a=3
    def fun(self,y):
        print y
    def prt(self,a):
        self.a=a+2
        print self.a
        
class old(new):
    def __init__(self,x,a):
        print x
        print new(a)
    def prt(self,y):
        self.y
        print self.y

         


z=old(1,3)
print z.__init__(2,5)
'''
print a.x,b.x
print a.y,b.y

def fun(n,o,m):
    total=new()
    total.x=n.x+o.x+m.x
    total.y=n.y+o.y+m.y
    return total.x,total.y
'''    