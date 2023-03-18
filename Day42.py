marks = [12, 45, 67, 23, 87, 85, 98, 45, 76]

for index, mark in enumerate(marks):
    print(mark)
    if(index==6):
        print("Akash, Awesome")

print()

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print()

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)