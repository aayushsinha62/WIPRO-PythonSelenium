#lambda - ananonymous nameless functions, oneline, simple operations

#syntax

lambda arguments: expression


#it can have any number of arguments
#must have only one expression
#the expression is automatically returned

#function - function name, arguments, return type, code

#normal function add 2 numbers

def add(a,b):
    return a+b

print(add(5,3))

#lambda function

add = lambda a,b: a+b
print(add(5,3))

#square of a number

square=lambda a: a*a
print(square(5))

#even or odd

even=lambda a: a%2==0
print(even(5))

#find max of two numbers

max=lambda a,b: a if a>b else b
print(max(5,6))

#filter, map and reduce in built functions in lambda

#filter - select data - filtering the data
# map - transform the data
# reduce - aggregate the data

#filter

numbers=[1,2,3,4,5]

evens=list(filter(lambda x: x% 2==0, numbers))
print(evens)

#filter the failed test cases

status=['pass', 'fail', 'pass', 'fail']
failed=list(filter(lambda s: s=="fail", status))
print(failed)

#filter positive numbers

nums = [-5, 10, -3, 7, 0, 2]
positive=list(filter(lambda p: p>=0, nums))
print(positive)

#filter non-empty strings

string=["hello", "world", ""]
nonempty=list(filter(lambda x: x!="", string))
print(nonempty)

#reduce - aggregate - combining many values to a one single result
#takes two arguments and returns single value

from functools import reduce

nums=[10,20,30,40]
print(reduce(lambda x,y: x+y, nums))

#multiply
print(reduce(lambda x,y: x*y, nums))

#getting max value
print(reduce(lambda x,y:x if x>y else y, nums))

#min value
print(reduce(lambda x,y:x if x<y else y, nums))

#map-transforms the data-function is applied to every element

nums=[10,20,30]

square=list(map(lambda x:x*x, nums))
print(square)

#sorting in lambda

data=[(1,3),(4,1),(2,2)]
sorteddata=sorted(data, key=lambda x:x[0])
print(sorteddata)

#it is sorting based on first means 0th element of each tuple

marks={"A":75, "B":80, "C":60}
sorted_marks=dict(sorted(marks.items(),key=lambda x:x[1]))
print(sorted_marks)

#it is sorting based of second element 1st of each tuple