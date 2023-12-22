class empl:
    name="rohit"
    rollno=66
    div="b"
    def info(self):
        print(f"{self.name} roll no {self.rollno} div {self.div}")

a=empl()
a.name="ram"
a.rollno=16
a.div="d"
print(a.div,a.rollno,a.name)
a.info()

#---------using constructor----------------
#---------parameterized constructor--------
class Person:
    def __init__(self,n,o):
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("rohit","developer")
a.info()
b=Person("ram","Analytics")
b.info()

#------default constructor------------
class lib:
    def __init__(self):
        print("which book you want.")

a=lib()

