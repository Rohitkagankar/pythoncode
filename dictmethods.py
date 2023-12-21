#dictionary methods

dict={"name":"rohit","age":22,"add":"pune"}
print(dict)
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.values())
for key in dict.keys():
    print(dict[key])

print(dict.items())

a1={1:11,2:22,3:33}
a2={4:44,5:55,6:66}
a1.update(a2)
print(a1)

a1.pop(1)
a1.popitem()
print(a1)
a1.clear()
del a1
print(a1)

