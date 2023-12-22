def greet(fx):
    def nfx(*args,**kwargs):
        print("good morning.")
        fx(*args,**kwargs)
        print("thank you.")
    return nfx
@greet
def hello():
    print("hello world")
hello()
print("---------new-----------")

def add(a,b):
    print(a+b)

greet(add)(5,3)

print("-----------new---------------")
def greet1(x):
    def fun(*args):
        print("hello, welcome")
        x(*args)
        print("thank you")
    return fun


@greet1
def cube(x):
    print(f"cube of {x} is : ",x*x*x)

cube(5)
#greet1(cube)(5)