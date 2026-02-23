#race condition means multiple threads accessing same resource without synchronization
#very important in interviews

import threading
count=0
lock=threading.Lock()

def increment():
    global count
    with lock:
        for _ in range(10000):
            count+=1

t1=threading.Thread(target=increment)
t2=threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(count)

#with lock - automatically acquires and releases the lock for every thread