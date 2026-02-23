#
#constructors - first function of the class which is called
#          when the object of the class is created
# syntax is __init__()

#we can parameterise the constructor
#self is mandatory


class Student:
    def __init__(self):
        print("constructor is called")

    def addsum(self):
        print("hi")

s1=Student() #object of student is created

#calling happens automatically to init constructor

s1.addsum()


#parameterized constructor

#self.name is a instance variable (belongs to object)
#name is a local parameter (Exists inside the method)
#if we dont assign it to the self, object will not remember the value

class Employee:
    def __init__(self, name,salary):
        self.name=name #assigning to self makes the variable global for the object to access else they just remain limited within method
        self.salary=salary

    def display(self):
        print(self.name, self.salary)


e1=Employee("aayush","50000")
e2=Employee("ravi","78000")
e1.display()
e2.display()


#using * args in constructor



#constructor overloading isnt directly supported, done by passing * argument
#constructors are used for preconditions



class Numbers:
    def __init__(self, *args):
        self.values=args

n=Numbers(10,20,30)
print(n.values)

n=Numbers(20,30)
print(n.values)

p=Numbers(3)
print(p.values)

#as i can pass any no. of parameters with * argument so constructor overloading is achieved


#parent and child constructors
#super keyword for accessing parent constructor

class Parent:
    def __init__(self):
        print("i am the parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am child constructor")

c=Child()

