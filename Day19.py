for i in range(12):
    if(i==10):
        print("Leaves Loop!")
        break
    print("5 X ",i+1,"= ", 5*(i+1))

print("\n\n")

for i in range(12):
    if(i==10):
        print("Skips Iteration!")
        continue
    print("5 X ",i+1,"= ", 5*(i+1))