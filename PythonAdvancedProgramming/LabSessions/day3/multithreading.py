#multithreading

import threading
import time

def numbers():
    for i in range(5):
        print("Number",i)
        time.sleep(0.2)

def letters():
    for k in "ABCDE":
        print("Letter",k)
        time.sleep(0.2)

t1=threading.Thread(target=numbers)
t2=threading.Thread(target=letters)

t1.start()
t2.start()

t1.join()  #makes current thread to wait until another thread finishes means until all threads get executed
t2.join()


print("thread terminated")