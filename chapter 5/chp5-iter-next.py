class new():
    def __init__(self,a):
        self.a=iter(a[::-1])

class reverse_iter(new):
    def next(self):
        return self.a.next()  


it=reverse_iter([1,2,3,4])
it.next()