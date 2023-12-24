class math:
    def __init__(self,val):
        self.value=val

    def fun(self,n):
        self.value=self.value+n

    @staticmethod
    def add(a,b):
        return a+b

a=math(4)
print(a.value)
a.fun(5)
print(a.value)
print(math.add(4,8))
print(a.add(44,33))