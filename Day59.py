# Decorators in Python
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank You!")
    return mfx

@greet
def hello():
    print("Hello World!")

@greet
def add(a, b):
    print(f"{a}+{b} = ",a+b)

# greet(hello)()
hello()
# greet(add)(3,4)
add(4, 5)