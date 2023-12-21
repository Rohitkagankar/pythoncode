def square(x):
    return x*x

l1=[1,2,3,4,5,6]
newList=[]
for num in l1:
    newList.append(square(num))
print(newList)

#------map-----
def cube(x):
    return x*x*x

l=[1,2,3,4,5,6]
n=list(map(cube,l))
n=list(map(lambda x: x*x*x, l ))
print(n)

#--------filter--------
def fun(a):
    return a>4
l2=[9,1,2,3,4,5,6,7,8,]
s=list(filter(fun,l2))
print(s)

#--------reduce------
from functools import reduce
m=[1,2,3,4,5,6,7,8,9]
newM=reduce(lambda x,y: x+y,m)
print(newM)
