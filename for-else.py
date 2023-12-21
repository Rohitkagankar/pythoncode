#for loop with else:

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("done with for loop")

i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("done with while loop")
