# Map, Filter and Reduce
# MAP
# def cube(x):
#     return x*x*x

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7]
# cubel = []
# for i in l:
#     cubel.append(cube(i))

cubel = list(map(lambda x: x*x*x, l))
print(cubel)

# FILTER
def filter_function(a):
    return a>4

newl = list(filter(filter_function, l))
print(newl)

# REDUCE
l2 = [1, 2, 3, 4, 5]
def sum(x, y):
    return x+y

s = reduce(sum, l2, 0)
print(s)