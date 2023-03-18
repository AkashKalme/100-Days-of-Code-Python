# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"The local variable is {x}")
#     print("Hello")

# print(f"The global variable is {x}")
# hello()
# print(f"The global variable is {x}")

# print()
# print()

x = 10

def fun():
    global x
    x = 5
    y = 7
    print("Running Function fun")

print(f"The global variable is {x}")
fun()
print(f"The global variable is {x}")
# print(y)