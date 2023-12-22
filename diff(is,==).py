#diff between is and ==

a=10
b=10
print(a is b)  #exact location of memory
print(a == b)  #value

c=[1,2,3,4]
d=[1,2,3,4]
print(c is d)
print(c == d)

a=(1,2,3,4)
b=(1,2,3,4)
print(a is b)
print(a == b)

a={1,2,3}
b={1,2,3}
print(a is b)
print(a == b)

a={"a":1, "b":2}
b={"a":1, "b":2}
print(a is b)
print(a==b)