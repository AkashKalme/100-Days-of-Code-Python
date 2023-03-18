# Multithreading in Python

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return seconds
    # print(f"Slept for {seconds} seconds.")

def main():
    # Normal Code
    # time1n = time.perf_counter()
    # func(4)
    # func(2)
    # func(3)
    # time2n = time.perf_counter()
    # print("Normal Time: ", time2n-time1n)
    # Code using Threads
    time1t = time.perf_counter()
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[3])
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    time2t = time.perf_counter()
    print("Threaded Time: ", time2t-time1t)

def poolingDemo():
    with ThreadPoolExecutor() as executer:
        # future = executer.submit(func, 4)
        # future = executer.submit(func, 2)
        # future = executer.submit(func, 3)
        # print(future.result())
        # print(future.result())        
        # print(future.result())
        l = [3,5,1,2,6]
        results = executer.map(func, l)
        for result in results:
            print(result)

poolingDemo()