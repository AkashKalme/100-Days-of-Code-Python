# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open('marks.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     mi = line.split(",")
#     mi1 = mi[0]
#     mi2 = mi[1]
#     mi3 = mi[2]
#     print(f"Marks of Student {i} in Math: {mi1}")
#     print(f"Marks of Student {i} in Science: {mi2}")
#     print(f"Marks of Student {i} in English: {mi3}")

f = open('myfile3.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3\n']
f.writelines(lines)
f.close()