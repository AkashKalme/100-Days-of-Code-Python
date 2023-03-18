import time
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
if(int(time.strftime('%H')) < 12 and int(time.strftime('%H')) >= 0):
    print("Good Morning, Sir!")
elif(int(time.strftime('%H')) > 11 and int(time.strftime('%H')) < 17):
    print("Good Afternoon, Sir!")
else:
    print("Good Evening, Sir!")

