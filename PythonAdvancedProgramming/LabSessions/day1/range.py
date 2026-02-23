# 1.
# Write
# a
# Python
# function
# to
# check
# whether
# a
# number
# falls
# within
# a
# given
# range.


def checkrange(num, start, end):

    if num>=start and num<=end:
        print("number is in range")
    else:
        print("number isnt not in range")

checkrange(5,1,6)
print("\n")





# 2.
# Write
# a
# Python
# function
# to
# Print
# even
# numbers
# from
#
# 1
# to
# 50
#

def printeven():
    for i in range(1,51):
        if i%2==0:
            print(i, end=",")

printeven()
print("\n")

# 3.
# Write
# a
# Python
# function
# to
# Sum
# of
# numbers
# from
# 1
# to
# 100

def sum():
 for i in range(1,101):
    total = 0
    total=total+i
 print(total)

sum()
print("\n")


#
# 4.
# Print
# all
# numbers
# divisible
# by
# 5
# between
# 1 and 100
#

for i in range(1,101):
    if i % 5 ==0:
        print(i, end=",")

print("\n")

# 5.
# Create
# a
# list
# of
# numbers
# from
#
# 50
# to
# 100
# with a step of 5

numbers=list(range(50,100,5))
print(numbers)

print("\n")


#
# 6.
# Print
# the
# square
# of
# each
# number
# from
#
# 1
# to
# 10.

for i in range(1,11):
    square=i*i
    print(square, end=",")

print("\n")

# 7.
# Print
# numbers
# between - 10 and 10.

for i in range(-10,11):
    print(i, end=",")
print("\n")

