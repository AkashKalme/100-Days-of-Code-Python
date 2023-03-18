# Tuple (Immutable)
tup = (1, 4, 7, 8)
print(type(tup))
print(tup)

tup2 = (4)
print(type(tup2))
print(tup2)

tup3 = (4,)
print(type(tup3))
print(tup3)

tp = (4,8,5,2,6,7,1,2,6)
print(tp[:])
print(tp[4])
print(tp[2:5])
print(tp[1:6:2])
print(tp[-5])

if 5 in tp:
    print('YES')

tp2 = tp[1:5]
print(tp2)