#-------def function----------
def double(x):
    return x*x
print(double(10))

def newValue(fx,value):
    return 6+ fx(value)

square=lambda x: x*x
print(newValue(square,5))


#-------lambda function--------
double1 =lambda x : x*x
cube= lambda x: x*x*x
avg=lambda x,y,z:(x+y+z)/3

print(double1(25))
print(cube(5))
print(avg(3,4,5))



