# Create
# a
# Car
#
#
# class with attributes brand, model, price.

class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

#
# Create
# a
# Student
#
#
# class with method get_grade() based on marks.

class Student:
    def __init__(self,marks):
        self.marks=marks

    def get_grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B"
        elif self.marks>=60:
            return "C"
        else:
            return "Fail"

#
# Create
# a
# BankAccount
#
#
# class with deposit() and withdraw() methods.

class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")
#
#
# Write
# a
#
#
# class Employee that initializes name, id, salary using __init__.
#
#

class Employee:

    def __int__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary


# Create
# a
#
#
# class that counts how many objects are created.

class ObjectCounter:
    count=0

    def __init__(self):
        ObjectCounter.count+=1

#
#
# Create
# a
#
#
# class Company with a class variable company_name.
#

class Company:

    company_name="Wipro"

#
# Implement
# a
# static
# method
# to
# validate
# email
# format.
#

class Validator:
    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email

#
# ✅ Inheritance
#
# Create
# a
# base
#
#
# class Vehicle and derived class Bike.
#

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is riding")

#
# Create
# Person → Employee → Manager(multilevel
# inheritance).
#


class Person:
    def __init__(self,name):
        self.name=-name

class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id

class Manager(Employee):
    def __init__(self,name,emp_id,department):
        super().__init__(name,emp_id)
        self.department=department

#
# Override
# a
# method in child
#
#
# class and call parent method using super().

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is child class")

obj=Child()
obj.show()

# ✅ Encapsulation
#
# Create
# a
#
#
# class BankAccount with private balance.
#
#
# Use
# getter and setter
# methods
# to
# update
# balance
# safely.
#
# Prevent
# negative
# salary
# using
# property
# decorators.

class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print("Balance cannot be negative")

acc=BankAccount(100)
print(acc.balance)

acc.balance=-700
print(acc.balance)


#
# ✅ Polymorphism
#
# Create
# a
# Shape
#
#
# class with method area().Implement Circle and Rectangle.
#
#

class Shape:

    def area(self):
        pass

class Circle(Shape):
    def _init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def rectangle(self):
        return self.length*self.breadth




# Demonstrate
# method
# overloading
# using
# default
# arguments.
#

class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c

calc=Calculator()
print(calc.add(5))
print(calc.add(5,6))

# Demonstrate
# operator
# overloading(__add__).
#

class Number:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
        return self.value+other.value

n1=Number(10)
n2=Number(20)
result=n1+n2
print(result)



# Create
# Engine
#
#
# class and use it inside Car class.
#
#

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine=Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")

car=Car()
car.drive()

# Create
# Team
#
#
# class that contains multiple Player objects.

class Player:
    def __init__(self,name):
        self.name=name

class Team:
    def __init__(self):
        self.players=[]

    def add_player(self,player):
        self.players.append(player)

    def show_players(self):
        for player in self.players:
            print(player.name)

p1=Player("Virat")
p2=Player("Rohit")
p3=Player("Rohan")
team=Team()
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

team.show_players()