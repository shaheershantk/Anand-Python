class minute():
    i='123'
    def minit(self,h):
        return h*60

y=minute()
a=input('>>')
print y.minit(a)
second=y.minit(a)*60
repr(minute())