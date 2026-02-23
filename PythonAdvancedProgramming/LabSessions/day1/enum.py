# Q1
# What is the
# output?
#
list(enumerate(['a', 'b', 'c']))

#[(0, 'a'), (1, 'b'), (2, 'c')]
#
#
# Q2
# What is the
# output?
#
for i, v in enumerate([10, 20, 30]):
    print(i, v)

#0 10
# 1 20
# 2 30

# Q3
# Write
# code
# to
# print
# index + value
# from:
#
# Index
# should
# start
# from
#
# 1.
#
colors = ['red', 'green', 'blue']

for i,color in enumerate(colors, start=1):
    print(i,color)

#
# Q4
# What is the
# output?
#
 list(enumerate("PYTHON", start=1))

# [(1, 'P'), (2, 'Y'), (3, 'T'), (4, 'H'), (5, 'O'), (6, 'N')]



#
# Q5
# Find
# the
# index
# of
# value
# 50
# using
# enumerate():
#
nums = [10, 20, 30, 40, 50, 60]
for i,nums in enumerate(nums):
    if nums==50:
        print(i)


#
# Q6
# What is the
# output?
#
for i, n in enumerate(range(10, 60, 10)):
    print(i, n)

# 0 10
# 1 20
# 2 30
# 3 40
# 4 50

#
# Q7
# Convert
# this
# into
# an
# enumerate()
# loop:
#
# for i in range(len(data)):
#     print(i, data[i])

for i,value in enumerate(range(len(data))):
  print(i, value)

#
# Q8
# What is printed?
#
items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)
#
# (0,'a')
# (1, 'b')
# (2, 'c')

# Q9
# What is the
# output?
#
list(enumerate([], start=5))

# [] because start value doesnt matter, no data to enumerate
#
# Q10
# What is the
# output?
#
for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

-1,100
0,200
1,300
#
# Q11
# What
# happens
# here?
#
i,v = enumerate(['x', 'y', 'z']):

error cant assign two variables like that

 for i,v in enumerate(['x', 'y', 'z']):
 print(i,v)

# 0,x
# 1,y
# 2,z
#
# Q12
# Explain
# the
# difference:
#
# enumerate(data)
# enumerate(data, start=1)

first once starts indexing from 0
second from 1
