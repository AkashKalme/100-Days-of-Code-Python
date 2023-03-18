s1 = {3,4,5,6,7}
s2 = {5,2,3,8}
s3 = {8,9,10,11}
s4 = {5,7}

print("Uniion: ",s1.union(s2))

print("Intersection",s1.intersection(s2))

print("Difference (s1-s2): ", s1.difference(s2))
print("Difference (s2-s1): ", s2.difference(s1))

print("Is Disjoint(s1 & s2)?", s1.isdisjoint(s2))
print("Is Disjoint (s1 & s3)?", s1.isdisjoint(s3))

print("Is Superset (s1 & s3)?", s1.issuperset(s3))
print("Is Superset (s1 & s4)?", s1.issuperset(s4))

print("Is Subset (s1 & s3)?", s3.issubset(s1))
print("Is Subset (s1 & s4)?", s4.issubset(s1))

print("Before Update: ",s1, s2)
s1.update(s2)
print("After Update: ",s1, s2)

s4.add(4)
print("s4: ",s4)

# s4.remove(3)
s4.remove(7)
print("s4: ",s4)

s4.discard(3)
print("s4: ",s4)

print("Popped from s2: ",s2.pop())
print("s2: ",s2)

if 8 in s2:
    print("Yes")
else:
    print("No")

del s1
# print(s1)