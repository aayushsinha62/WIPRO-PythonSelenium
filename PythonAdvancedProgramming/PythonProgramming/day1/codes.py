# Write
# a
# Python
# program
# to
# get
# the
# largest
# number
# from a list.
#

numbers=[10,45,60,70,23]
largest=numbers[0]

for num in numbers:
    if num>largest:
        largest=num

print(largest)

#
# remove
# the
# even
# numbers
# from the lost
#

result=[]
for num in numbers:
    if num%2!=0:
        result.append(num)

print(result)

# multiply
# the
# items in the
# list


result=1
for num in numbers:
    result=result*num

print(result)