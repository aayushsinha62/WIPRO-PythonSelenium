
#all numbers should be integers
#step size cannot be zero
#start default 0
#stop ending number is not included
#increment decrement default 1
#range doesnt create list - creates object
#fast iteration
#used for loops and indexing
#counters are clear to understand



a=range(5)
print(a[1])
print(a[3])

# for loop for range of 2 arguements
a1=range(2,5)
print(a1[1])

# for loop for range of 3 arguements
a=range(2,5,-3)
for i in a:
    print(i)

a= range(2, 5, 1)
for i in a:
 print(i)

# scenario : account system

for attempt in range(3):
    pin=input("Enter the pin:")
    if pin=="1234":
        print("Access granted")
        break
    else:
        print("Try again")


    # scenario: apply dis based on position of item

    prices=[100,200,300,400]
    for i in range(len(prices)):
        if i&2==0:
            print("discount applied on item ")

#scenario scheduler simulate polling every sec for 10 secs

import time
for second in range(10):
    print("checking status at {second}")
    time.sleep(1)