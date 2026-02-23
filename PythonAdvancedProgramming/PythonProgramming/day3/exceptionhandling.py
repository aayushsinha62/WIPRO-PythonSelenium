
#done so that one runtime error doesnt stop the whole normal flow of program
#and it doesnt crash

#done using try except #try catch in java

#helps in debugging
#prevents program crashing
#handling errors and exceptions in the code more efficiently

#try - code to be executed
#except - exceptions details catching
#else - if exception doesnt occur then else part will be executed
#finally - mandated/compulsory code to execute even if exception comes
          #or doesnt come

#custom exceptions #prints error

try:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    print(a/b)

except ZeroDivisionError:

    print("cannot divide by zero")

except ValueError:

    print("please enter valid numbers")


#generic exception #built in exception #just returns the error

try:
    a=5/0

except Exception as e:
    print(e)

else: #runs only if no exception occur
    print("division successful")

finally:
    print("close the browser")


#raise exception is used when python doesnt raises the error automatically
# we need to handle manually for cases like age less than 18

age=int(input("Enter the age"))

if age<18:
    raise ValueError("age must be 18 or above")

