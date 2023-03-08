a=(1,2.5,True,"MHD")
print(a)
print(type(a))
print(a[1])
print(type(a[1]))

b=list(a)
print(b)
b.append("Mohamed")
print(b)
print(type(b))
c=tuple(b)
print(c)
print(type(c))

print("===================================================")
for i in a:
    print(i)

if "Anshaf" in a:
    print("MHD is Found")
else:
    print("NotFound")

print("===================================================")

# a=(1,)
# print(type(a))
# del a
# print(a)

print("===================================================")
a=(1,2,3,4)
b=(5,6,7,4)
c=a+b
print(c)
print(c.count(1))

print("===================================================")
a=(1,2,3,4)
b=(5,6,7,4)
c=(a,b)
print(c)
print(c[1])
print(c[1][2])

print("===================================================")
x=("MHD",)*10
print(x)

a=(1,2,3,6)
print(a)
print(max(a))
print(min(a))
