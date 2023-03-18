# 'is' vs '=='
a = 4
b = "4"
print(a is b)   # Exact Location of Object
print(a==b)     # Value

c = [1, 4, 3]
d = [1, 4, 3]
print(c is d)
print(c==d)

e = 5
f = 5
print(e is f)
print(e==f)

g = (1, 2)
h = (1, 2)
print(g is h)
print(g==h)

i = None
j = None
print(i is j)
print(i is None)
print(i==j)