#factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#figonacy
def figo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return figo(n-1)+figo(n-2)
print(figo(1))
print(figo(2))
print(figo(10))
