# #sets
# s={"rohit",1,3,2,4,5,1,1,1,2}
# for value in s:
#     print(value)
#
# set1=set()
# print(type(set1))

s1={1,2,3,4}
s2={3,4,5,6,7,8}
print(s1.symmetric_difference(s2))
print(s1.union(s2))
s1.update(s2)
s1.intersection_update(s2)
print(s1.issubset(s2))
s1.remove(4)
s1.discard(11)
print(s1)
s3=s1.pop()
print(s1,s2)
print(s3)
s1.clear()
print(s1)
print(s3)
del s3
print(s3)
