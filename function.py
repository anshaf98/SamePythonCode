def welcome():
    print("Welcome to...")

welcome()

# def add():
#     a=int(input("Enter Value A:"))
#     b=int(input("Enter Value b:"))

#     c=a+b
#     print(c)

# add()

# def sub(a,b):
#     c=a-b
#     print(c)

# sub(25,24)

# def mul():
#     a=int(input("Enter Value A:"))
#     b=int(input("Enter Value b:"))

#     c=a*b
#     return c

# x=mul()
# print(x)

# def div(a,b):
#     c=a/b
#     return c

# x=div(25,24)
# print(x)

print("============================================")

def class1(*students):
    print(students)
    for user in students:
        print(user)

class1("Anshaf","MHD","Mohamed")

print("============================================")

def message(name,age):
    print(name," ",age)

message("Anshaf",23)
message(age=23,name="Anshaf")

print("==================**==========================")
def bio(**data):
    print(data)

bio(name="Anshaf",age=23,gender="Male")

print("=====================default=======================")
def user(name,city="Kinniya"):
    print(name," ",city)

user("Anshaf","Kinniya1")
user("Anshaf")

print("=====================passing list=======================")
def total(marks):
   return sum(marks)

print(total([55,20,12,35]))

print("====================1*2*3*4*5=120========================")
"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
1*2*3*4*5=120
"""

def factorial(x):
  if x==1:
      return 1
  else:
      return (x*factorial(x-1))

print(factorial(5))

print("============================================")

c=lambda a:a+500
print(c(5))

c=lambda a,b:a*b
print(c(10,69))