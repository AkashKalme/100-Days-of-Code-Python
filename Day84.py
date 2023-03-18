# Time Module in Python
import time
# def usingWhile():
#     i = 0
#     while i<5000:
#         i = i+1
#         print(i)
#     pass

# def usingFor():
#     for i in range(5000):
#         print(i)
#     pass

# init = time.time()
# usingWhile()
# t1 = time.time() - init
# init  = time.time()
# usingFor()
# t2 = time.time() - init
# print("Using While: ",t1)
# print("Using For: ",t2)

# print("3 Seconds")
# time.sleep(3)
# print("Printed after 3 seconds.")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)