def avg(a,b):
    mean=(a+b)/2
    print(mean)

avg(3,5)
avg(88,48)

def isGreater(a,b):
    if(a>b):
        print(a,"is greater")
    elif(a==b):
        print("eqal numbers")
    else:
        print(b,"is greater")
isGreater(33,37)

def calsum(a,b):
    pass

calsum(3,5)
print("hi")

# argument passing
# default ,keyword, variable length, required

def avg(a=5,b=4):
    print("avarage of ",a,"&",b,"is","=",(a+b)/2)

avg()     #default
avg(5,6) #required
avg(b=10,a=6)  #keyword

def average(*numbers):  #tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is : ",sum/len(numbers))
average(5,5,5,5)

def name(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])

name(mname="rajaram", fname="rohit", lname="kagankar")


    

















