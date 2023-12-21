file1=open('file.txt','r')
data=file1.read()
print(data)
file1.close()

f=open('file.txt','w')
f.write("Rohit you are good boy.")
f.close()

f=open('file.txt','a')
f.write("\nhe is an engineer")
f.close()

with open('file.txt','a') as f1:
    f1.write("\nhe got 1 core package.")

#-------read line by line text-------------
f2=open('file.txt','r')
while True:
    data=f2.readline()
    if not data:
        break
    print(data)
f2.close()

f3=open('file1.txt','r')
i=0
while (True):
    i=i+1
    line=f3.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"student {i} marks in english is : {m1}")
    print(f"student {i} marks in marathi is : {m2}")
    print(f"student {i} marks in hindi is : {m3}")
f3.close()
#----------write line-----------

f11=open('file.txt','w')
line=("line1\nline2\nline3\nline4")
f11.write(line)
f11.close()

#-------seek file---------

with open('file.txt','r') as f22:
    f22.seek(3)
    print(f22.tell())
    data=f22.read(3)
    print(data)
    f22.truncate()

#------truncate-------
with open('file.txt','w') as a:
    a.write("hello world")
    a.truncate(5)

with open('file.txt','r') as a:
    data=a.read()
    print(data)

