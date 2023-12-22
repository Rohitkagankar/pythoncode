class myclass:
    def __init__(self,value):
        self.val=value

    def show(self):
        print("value is : ",self.val)

    @property
    def geter(self):
        return 10*self.val

    @geter.setter
    def getter(self, newval):
        self.val=newval


p=myclass(2)
p.getter=5
print(p.getter)
p.show()
