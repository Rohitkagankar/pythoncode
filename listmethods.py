#lists methods
l=[4,5.6,4,3,4,6]
print(l)
print(type(l))
l[0]=6
print(l[0:])

list=[i for i in range(11) if i%2==0]
print(list)

l=[4,6,3,2,1,7,9]
print(l)
l.append(5)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(6))
m=l.copy()
m[0]=0
l.insert(7,"rohit")
p=[4,5,3,2,6,8,9,11]
l.extend(p)
print(l)
k=l+p
print(k)
