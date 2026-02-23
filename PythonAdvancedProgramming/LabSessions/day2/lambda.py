# 1
# nums = [1, 2, 3, 4, 5, 6]
#
# From
# a
# list
# of
# numbers:
# Filter
# even
# numbers
# Square
# them
# Find
# their
# sum

from functools import reduce
nums = [1, 2, 3, 4, 5, 6]

result=reduce(lambda x,y:x+y,
              map(lambda x: x*x,
                  filter(lambda x: x%2==0,nums)))

print(result)



#
# 2.
# salaries = [25000, 40000, 32000, 18000]
#
# rom
# a
# list
# of
# salaries:
# Filter
# salaries > 30, 000
# Add
# 10 % hike
# Find
# the
# total
# payout
#

from functools import reduce

salaries = [25000, 40000, 32000, 18000]

total_payout = reduce(
    lambda x, y: x + y,
    map(lambda x: x * 1.10,
        filter(lambda x: x > 30000, salaries)))

print(total_payout)

