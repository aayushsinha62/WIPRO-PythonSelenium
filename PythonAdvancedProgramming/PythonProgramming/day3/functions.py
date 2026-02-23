#functions is a block of code that performs specific task
#written  by def functionname()
from multiprocessing.util import sub_debug


def printdata():  #function/method signature
    print("Hello world")

printdata()  #calls the function


#function with parameters

def printdata(name):
    print("My name is", name)

#passing the arguement

printdata("Aayush")
printdata("Tina")

#return statement
#to return the function value return statement is used
#mainly used to return values in diff files and classes

def squareroot(number):
    result=number*number
    return result

#function call

square=squareroot(4)
print(square)

#function pass
#used to bypass a function when it is not used

def func_pass():
    pass

#call the function

func_pass()

#multiple return values

def cal(a,b):
    return a-b, a+b, a*b

sub,add,mul=cal(10,5)
print(add)
print(sub)
print(mul)

#functio calling an another function

def areaofrectangle(len,width):
    return len*width

def areaofsquare(side):
    return side*side

value=areaofrectangle(4,6)
sq=areaofsquare(value)
print(sq)


#function with a loop

def even(limit):
    for i in range(2,limit+1,2):
        print(i)

even(10)


#function with if else condition


def even(limit):
    if limit%2==0:
        return "even"
    else:
        return "odd"

print(even(10))
print(even(11))
