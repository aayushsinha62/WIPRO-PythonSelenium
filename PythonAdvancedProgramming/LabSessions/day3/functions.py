# # 1.
# # Write
# # a
# # Python
# # function
# # to
# # sum
# # all
# # the
# # numbers in a
# # list.

def sum_list(numbers):
    total=0
    for i in numbers:
        total=total+i
    return total

print(sum_list([1,2,3,4,5]))


# 2.Write a Python function to find the maximum of three numbers.
#
#

def max(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(max(1,2,2))