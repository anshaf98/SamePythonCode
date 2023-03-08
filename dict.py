user={
    "name":"Anshaf",
    "age":25,
    "isMarried":True
}

print(user)
print(type(user))
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

# for x in user:
#     print(x)
#     print(user[x])
for x in user:
    print(x," ",user[x])

print("=====================================================")
for x in user.values():
    print(x)

print("=====================================================")
for x in user.keys():
    print(x)

print("=====================================================")
for x,y in user.items():
    print(x,y)

print("=====================================================")
if "age" in user:
    print("Present")

print("=====================================================")
user.update({"gender":"male"})
print(user)
user["age"]=24
print(user)

user.pop("age")
print(user)
user.clear()
print(user)

users={
    "user1":{
        "name":"Anshaf",
        "age":24,
        "isMarried":False
    },
    "user2":{
        "name":"Mohamed",
        "age":24,
        "isMarried":True
    },
    "user3":{
        "name":"MHD",
        "age":24,
        "isMarried":True
    }
}

print(users)