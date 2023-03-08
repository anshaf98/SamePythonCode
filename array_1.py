
# a=[1,2,3,4,5]
# print(a)
# print(type(a))

# a[0]=100
# print(a)
# print(a[1])
# print(a[-1])
# print(a[0:3])
# print(a[2:])
# print(a[:3])

# a=[1,True,"Anshaf",2.5,[1,2,3,4]]
# print(a)
# print(type(a))
# print(a[0])
# print(type(a[0]))
# print(type(a[1]))
# print(type(a[2]))
# print(type(a[4]))
# print(a[4][1])

# a=[10,25,35,45]
# print(a)
# a.clear()
# print(a)
# a=[10,25,35,45]
# b=a.copy()
# print(b)
a=[10,25,25,35,45]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop(0)
print(a)

a=[10,25,25,35,45]
a.remove(25)
print(a)

print("================================================")
name=["MHD"]
print(name)

name.append("Anshaf")
name.append("Mohamed")
name.append("mfm")
print(name)

name1=["anshaf","mohamed"]
name.extend(name1)
print(name)
name.insert(0,"MHDUpdate")
print(name)

print("================================================")
print(list(range(5)))
print(list("mohamed"))

a=[1,2,9,8,3,4]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["black","white","blue","apple"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=["black","white","blue","apple"]
a.sort(key=len)
print(a)