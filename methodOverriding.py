class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y

class newShape(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14 * super().area()

sq=shape(3,4)
print(sq.area())
a=newShape(5)
print(a.area())
