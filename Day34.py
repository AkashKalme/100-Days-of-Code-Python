ep1 = {122: 45, 234:67, 56: 99, 79:85, 79:67}
ep2 = {312: 55, 654:76, 123: 87}

print("Before Update EP1: ", ep1)
ep1.update(ep2)
print("After Update EP1: ", ep1)

print("Befroe Clear EP2: ", ep2)
ep2.clear()
print("After Clear EP2: ", ep2)

empt = {}
print("Empty Dictionary: ", empt)

print("Before popping 234: ", ep1)
ep1.pop(234)
print("After popping 234: ", ep1)

print("Before popping a item: ", ep1)
ep1.popitem()
print("After popping a item: ", ep1)

ep3 = {34:56, 67:89}
print("Before Deletion: ", ep3)
del ep3
# print("After Deletion: ", ep3)

ep4 = {34:56, 67:89, 56:22}
print("Before Deletion of key 67: ", ep4)
del ep4[67]
print("After Deletion of key 67: ", ep4)