# Generators in Python
# Generators in Python are special type of functions that allow you to create an iterable sequence of values.

def my_generator():
    for i in range(20):
        yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)