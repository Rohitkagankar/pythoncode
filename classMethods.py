class employee:
    company="Google"
    def show(self):
        print(f"{self.name} works in {self.company}")

    @classmethod
    def ccn(self,ncompany):
        self.company=ncompany

a=employee()
a.name="rohit"
a.show()
b=employee()
b.name="ram"
b.ccn("apple")
b.show()
print(employee.company)

#class methods as alternative constructors in python
print("------------------------------")
class person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print(f"{self.name} has {self.salary} salary.")
    @classmethod
    def strinput(self,string):
        return self(string.split("-")[0],string.split("-")[1])

a=person("rohit",12000)
a.show()

string="ram-15000"
b=person.strinput(string)
print(b.name,b.salary)
b.show()