# cerate a python program with class name savingsccount and functions deposit in parent class  and  addinterest in the child class

class savingsaccount:

    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("deposited",amount)
        print("balance after deposit",self.balance)


class InterestAccount(savingsaccount):
    def addinterest(self,rate):
        interest=self.balance*rate/100
        self.balance=self.balance+interest
        print("final balance",self.balance)

acc=InterestAccount(1000)
acc.deposit(100)
acc.addinterest((5))


# 1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())



# 2.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob as (year, month, day)

    def age(self):
        today = date.today()
        birth_date = date(self.dob[0], self.dob[1], self.dob[2])
        return today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )


# Example usage
p = Person("Aayush", "India", (2002, 5, 10))
print("Age:", p.age())



# 3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Example usage
t = Triangle(3, 4, 5)
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())



# 4.Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)


class Bus(Vehicle):
    pass


# Example usage
b = Bus("Volvo", 80)
b.show()



# 5.Write a python program to create  a Vehicle class without any variables and methods

class Vehicle:
    pass


# Example usage
v = Vehicle()
print(v)
