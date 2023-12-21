# if else statement
age=int(input("Enter your age: "))
print("your age is : ",age)

if age>18:
    print("you can drive")
else:
    print("you are small")

name = "rohit"
colors=["red","blue","pink"]
for i in name:
    print(i)
    if(i=="h"):
        print("this is nice")

for col in colors:
    print(col)

for k in range(0,11,2):
    print(k)

# while loop
i=int(input("enter the number: "))
while(i<=5):
    print(i)
    i=i+1
print("done with loop")


i=int(input("enter the number: "))
while(i<=50):
    i = int(input("enter the number: "))
    print(i)
print("thank you")

count=5
while(count > 0):
    print(count)
    count = count-1
else:
    print("I am inside else")

for i in range(15):
    if i==0:
        continue
    print("5 X",i,"=",5*i)
    if i==10:
        break
print("end of loop")

i=0
while True:
    i = i + 1
    print(i)

    if(i==10):
        break