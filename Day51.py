# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(17)
#     print(f.tell())
#     data = f.read(6)
#     print(data)

with open('myfile4.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)

with open('myfile4.txt', 'r') as f:
    print(f.read())