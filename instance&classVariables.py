class emplooyee:
    company="Google"  #class variable
    noOfemployee=0
    def __init__(self,name):
        self.name=name
        self.raiseSalary=0.3 #instance variables
        emplooyee.noOfemployee +=1

    def empDetails(self):
        print(f"employee {self.name} works in {self.noOfemployee} sized {self.company} company and salary raise is {self.raiseSalary} percent.")

a=emplooyee("Rohit")
a.empDetails()
a.raiseSalary=0.5
a.company="Apple"
a.empDetails()
emplooyee.empDetails(a)
b=emplooyee("ram")
b.empDetails()


