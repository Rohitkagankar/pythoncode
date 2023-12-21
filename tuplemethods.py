#tuple not changable
# tup=(3,4,6,7,8)
# print(type(tup),tup)
#
# print(tup[0])
# print(tup[0:7])
# l=(1,2,3,4,5)
# m=(6,7)
# k=l+m
# print(k)

name=("rohit","ranjit","sunita","ram","sakshi")
temp=list(name)
temp.append("devdas")    #add
temp.pop(3)              #remove
temp[0]="Rohit"          #change
name=tuple(temp)
print(name)

t1=(3,3,3,4,5)
t2=(1,1,1,2,3,3,3)
t3=t1+t2
print(t3)
print(t1.count(3))
print(t1.index(5))
print(t2.index(1))
print(len(t2))