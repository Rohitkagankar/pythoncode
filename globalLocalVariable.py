#global local variable
x=10  #global variable
y=5   #global variable

def addition():
    x=20  #local variable
    sum=x+y
    print(sum)
    print(x)

addition()
print(x)
print(y)

