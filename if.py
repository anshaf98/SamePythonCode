# a=int(input("Enter value:"))

# if a%2==0:
#     print(a,"is Even Number")
# else:
#     print(a,"is Odd Number")

# name=input("Enter name:")
# age=int(input("Enter age:"))

# if age>=18:
#     print(name,"age is",age,"Yes")
# else:
#    print(name,"age is",age,"No")

'''
0 - fine
1-5 - 0.5
5-10 - 1
10-30 - 5
30 - Cancel
'''

# day=int(input("Enter days:"))

# if day==0:
#     print("good and fine")
# elif day>=1 and day<=5:
#    print("Fine Amount:",day*.5)
# elif day>=5 and day<=10:
#    print("Fine Amount:",day*1)
# elif day>=10 and day<=30:
#    print("Fine Amount:",day*5)
# else:
#    print("Canceled")

'''
3 mark input
Total
Average
Res

90-100 - A
80-89 - B
70-79 - C
Else - D
'''

m1=int(input("Enter Mark:"))
m2=int(input("Enter Mark:"))
m3=int(input("Enter Mark:"))

total=m1+m2+m3
avg=total/3
print(total)
print(avg)

if m1>=35 and m2>=35 and m3>=35:
    print("Pass")
    if avg>=90 and avg<=100:
        print("A")
    elif avg>=80 and avg<=89:
        print("B")
    elif avg>=70 and avg<=79:
        print("C")
    else:
        print("D")
else:
   print("Fail")
   print("No Grade")