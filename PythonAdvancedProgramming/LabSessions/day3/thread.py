#thread smallest lightweight unit of execution within a process

#multithreading - execution of multiple threads at a time

#threading needs to be imported

#simple thread

import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

t=threading.Thread(target=task)
t.start()
t.join()

print("thread terminated")



