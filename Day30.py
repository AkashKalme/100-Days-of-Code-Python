def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

x = int(input("Number: "))  
print("Factorial: ",factorial(x))

def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)

y = int(input("Number: "))
print("Fibonacci: ", fibonacci(y))