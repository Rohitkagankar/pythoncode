marks=[80,45,56,77,99,74,85]

index=0
for val in marks:
    print("| " ,val," |")
    if index==4:
        print("99, you are first")

    index+=1

print("-----------new----------------")
for index ,val in enumerate(marks):
    print(val)
    if index==4:
        print("you are first")

#----------import----------------
from math import sqrt as sq,pi
# import math
print(dir(sq))
a=9
print(sq(a)*pi)