class oldclass:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"the name of emp id {self.id} is {self.name}.")

class newclass(oldclass):
    def showDetails1(self):
        print("he is python programmer.")

a=oldclass("rohit",11)
a.showDetails()

b=newclass("ranjit",22)
b.showDetails()
b.showDetails1()



#------new-------

class parent:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
    def showdetails(self):
        print(f"the name of emplyee is {self.name} and occupation is {self.occ}.")

    def welcome(self):
        print("welcome")

class child(parent):

    def cdetails(self):
        print("thank you...")


a=parent("rohit","developer")
a.showdetails()

c=child("ram","scientist")
c.showdetails()
c.cdetails()



