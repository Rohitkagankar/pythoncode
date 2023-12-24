#dir, __dict__,help methods
x=[1,2,3,4]
print(dir(x))


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.city="kolhapur"
    def show(self):
        print(f"{self.name} has {self.age} age he is from {self.city}")

a=person("rohit",22)
a.show()
print(a.__dict__)

print(help(a))
print(help(person))