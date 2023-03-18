# Lambda Functions

# Normal Function
# def double(x):
#     return x*2
# print(double(5))

# Lambda Function
double = lambda x: x*2
square = lambda x: x*x
cube = lambda x: x*x*x
avg2 = lambda x, y: (x+y)/2
avg3 = lambda x, y, z: (x+y+z)/3
print(double(5))
print(square(5))
print(cube(5))
print(avg2(3,5))
print(avg3(5, 10, 6))

def appl(fx, value):
    return 6+fx(value)

print(appl(cube, 5))