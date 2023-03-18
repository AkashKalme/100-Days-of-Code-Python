# a = int(input("Enter Your Age: "))
# print("Yuor Age is: ", a)

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("Yes")
#     print("You can Drive")
# else:
#     print("No")
#     print("You cannot Drive") 

# applePrice = 210
# budget = 200
# if(applePrice<=budget):
#     print("Alexa, add 1kg apples to the cart.")
# else:
#     print("Alexa, do not add apples to the cart.")

# applePrice = 140
# budget = 200
# if(budget-applePrice > 50):
#     print("Alexa, add 1kg apples to the cart.")
# elif(budget-applePrice>70):
#     print("Its OK, you can buy.")
# else:
#     print("Alexa, do not add apples to the cart.")

# num = int(input("Enter a Value: "))
# if(num<0):
#     print("Negative")
# elif(num==0):
#     print("Zero")
# elif(num==999):
#     print("Special")
# else:
#     print("Positive")

# print("Happy")

n = int(input("Enter n: "))
if(n<0):
    print("Negative")
elif(n>0):
    if(n<=10):
        print("Between 1-10")
    elif(n>10 and n<=20):
        print("Between 110-20")
    else:
        print("Greater than 20")
else:
    print("Zero")