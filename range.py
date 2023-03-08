

# print(list(range(5)))
# print(list(range(2,5)))
# print(list(range(0,20,2)))
# print(list(range(0,20,1)))

# for i in range(1,20):
#     print(i)

# for i in range(5):
#     a=int(input("Enter a no:"))
#     b=int(input("Enter a no:"))
#     print(a+b)

for i in range(6):
    for j in range(i):
        print("*",end="")
    print("")

print("==========================")

for i in range(6,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("==========================")

# for i in range(95,101,1):
#     print(i)

print("==========================")
# A-Z = 65-90
# a-z = 97-122

# for i in range(65,71,1):
#     print(chr(i))

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")