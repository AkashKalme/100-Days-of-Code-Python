# Walrus Operator
# Allows you to assign value to an operator within an expression
a = True
print(a := False)

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

# names = ["John", "Jane", "Jim"]
# if (name := input("Enter a name: ")) in names:
#     print(f"Hello, {name}!")
# else:
#     print("Name not found.")

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)