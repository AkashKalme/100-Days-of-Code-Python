dic = {"Harry": "Human Being", "Spoon":"Object"}
print(dic)
print(dic["Harry"])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 
print(info.keys())
print(info.values())

print()
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

print()
print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}") 

emp = {12:"Akash", 34:"Ram", 65:"Sameesh", 54:"Zakir"}
print(emp)
# print(emp[35])
print(emp.get(35))