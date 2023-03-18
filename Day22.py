# Lists
marks = [3, 5, 6, "Harry", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-2])
print(marks[-1])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Grey" in colors:
#     print('Found!')
# else:
#     print('Not Found!')
if "Gre" in colors:
    print('Found!')
else:
    print('Not Found!')
# if "Gre" in "Green":
#     print("True")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:])
print(animals[3:6])
print(animals[6:])
print(animals[-4:])
print(animals[-3:-7:-1])
print(animals[1:7:3])

lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2==1]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
