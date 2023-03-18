x = int(input("Enter a value between 5 and 9: "))

if(x>9 or x<5):
    raise ValueError("Value should lie between 5 and 9.")