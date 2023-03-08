'''
name=input("Enter name:")
print(type(name))
print(name)
'''

'''
a=input("Enter Value 1:")
b=input("Enter Value 2:")
c=a+b

print("Total:",c)
'''

'''
a=int(input("Enter Value 1:"))
b=int(input("Enter Value 2:"))
c=a+b

print("Total:",c)
'''
'''
a=float(input("Enter Value 1:"))
b=float(input("Enter Value 2:"))
c=a+b

print("Total:",c)
'''

# name1,name2,name3=input("Enter 3 Names").split()
# name1,name2,name3=input("Enter 3 Names").split(",")
# print("Name 1:",name1)
# print("Name 2:",name2)
# print("Name 3:",name3)
# print("Full Name:",name1," ",name2," ",name3)

# a="Anshaf Mohamed"
# print(a)
# a='''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'''
# print(a)

# para=[25,20,25]
# para1=["25","20","25"]
# print(type(para))
# print(para)
# print(para[0])

# print(','.join(para1))

# para=[]
# print("Enter a para")

# while True:
#     line=input()
#     if line:
#         para.append(line)
#     else:
#         break
#     print(para)
#     output="\n".join(para)

#     print(output)

# a = 10.0
# print(a)
# print(type(a))

# b=int(a)

# print(b)
# print(type(b))

# a=int(input("Enter Value 1:"))
# b=int(input("Enter Value 2:"))
# c=a+b

# print("Total:",str(c))

# ! String and String Function
# a="Mohamed anshaf"
# print(a)
# print(type(a))
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.count("a"))
# print(a.endswith("af"))
# print(a.find("a")) 
# print(a.find("a",5))
# print(a.replace("a","A"))

# b="MHD07"
# print(b.isupper())
# print(b.islower())
# print(b.isalnum())
# print(b.isalpha())

# c="he\nis\nGood"
# print(c)
# print(c.splitlines())
# print(c.splitlines(True))

# c="he is Good"
# print(c.split(" "))

# d="he,is,Good"
# print(d.split(","))

# d="     GOOD     "
# print(len(d))
# print(len(d.strip()))
# print(len(d.lstrip()))
# print(len(d.rstrip()))

a="13-05-1998"
print(a.partition("-"))