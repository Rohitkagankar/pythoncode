#program to raise errors
a=int(input("enter the val between 2 and 5: "))
if(a<2 or a>5):
    raise ValueError("val should be bet 2 and 5")

a=input("enter string: ")
if(a != "quite"):
    raise ValueError("string should be \"quite\" ")