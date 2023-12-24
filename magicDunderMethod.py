#magic dunder methods------

class person:
    name="rohit"
    def __len__(self):
        #print(len(self.name))
        c=0
        for char in self.name:
            c=c+1
        return c

a=person()
print(a.name)
# a.name="ram"
print(len(a))

#--------------------------------
class person:
    def __init__(self):
        self.name="rohit"
        self.car="fz"
        print(f"{self.name} loves to ride {self.car} bike.")

a=person()

#---------------------------------
class ceo:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"the name of the ceo is {self.name} str"
    def __repr__(self):
        return f"the name of the ceo is {self.name} repr"
    def __call__(self):
        print("hello welcome")

a=ceo("rohit")
#print(a.__str__())
print(a)              #if str is present then execute otherwise execute repr
print(str(a))
print(repr(a))
print(a)
a()     #call method is executed