class school:
    def info(self):
        self.cname="jspm"
        self.cityc="pune"
    def show(self):
        print(f"the {self.cname} college is located in {self.cityc}.")

class student(school):
    def info(self):
        self.name="rohit"
        self.city="kolhapur"

    def show(self):
        super().info()
        print(f"the {self.name} took addmision in {self.cname} college.")
        super().show()

a=school()
a.info()
a.show()

b=student()
b.name="ram"
b.city="mumbai"
b.show()

#----------another-----------

class person:
    def __init__(self):
        self.name="rohit"
        self.id=1234
        print(f"{self.name} has id {self.id}.")

class programmer(person):
    def __init__(self,lang):
        self.lang=lang
        super().__init__()
        print(f"{self.name} has id {self.id} learning {self.lang} language.")

#a=person()
b=programmer("python")