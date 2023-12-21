a=input("enter the number: ")
print(f"multiplication table of {a} is : ")
try:
    for i in range(11):
        print(f"{int(a) * i}")
except Exception as e:
    print(e)

print("some imp lines of code")
print("end of program")

try:
    num=int(input("enter the integer: "))
    print(num)
except  ValueError:
    print("enter valid integer")

try:
    l=[1,2,3,4,5,6]
    i=int(input("enter the index: "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed")

def func1():
    try:
        l=[3,4,5,6,7]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("I am always executed...")

x=func1()
print(x)

