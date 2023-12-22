#-----------public------------------
class info:
    def __init__(self):
        self.name="rohit"

a=info()
print(a.name)    #public

#-------------private---------------
class new:
    def __init__(self):
        self.__city="kolhapur"
s=new()
#print(s.__city)       #private
print(s._new__city)
print(a.__dir__())

#--------protected------------
class student:
    def __init__(self):
        self._name="rohit"
    def fun(self):
        return "code with rohit"
class data(student):
    pass
a=student()
b=data()
print(a._name)
print(a.fun())
print(b._name)
print(b.fun())