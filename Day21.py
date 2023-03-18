# Keyword Arguments
def average(a, b):
    print("The average is ", (a+b)/2)
average(4, 6)

# Default Arguments
def average2(a=5, b=5):
    print("The average2 is ", (a+b)/2)
average2()
average2(4)
average2(b=7)

# Variable Length Arguments
def average3(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)
avg3 = average3(4,8,6,2)
print('Average3 is ', avg3)

# Dictionary as Argument
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")