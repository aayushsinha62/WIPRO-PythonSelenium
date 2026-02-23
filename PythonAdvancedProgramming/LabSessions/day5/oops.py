# Lab
# 1: Method
# Overriding
# with Inheritance
#     Create
#     a
#     base
#
#
#     class Employee with a method calculate_salary().
# Create
# a
# subclass
# Manager
# that
# overrides
# calculate_salary() and adds
# a
# bonus.
# Demonstrate
# runtime
# polymorphism
# using
# parent
#
#
# class reference.


class Employee:
    def calculate_salary(self):
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        base_salary=super().calculate_salary()
        bonus=10000
        return base_salary+bonus

emp:Employee=Manager()
print(Employee.calculate_salary())








# Lab
# 2: Polymorphism
# Using
# Function
# Arguments
# Create
# classes
# Dog, Cat, and Cow
# each
# with a method speak().
# Write
# a
# function
# animal_sound(obj)
# that
# calls
# speak().
# Pass
# different
# objects
# to
# the
# same
# function.
#

class Dog:
    def speak(self):
        return "Bark"


class Cat:
    def speak(self):
        return "Meow"


class Cow:
    def speak(self):
        return "Moo"


def animal_sound(obj):
    print(obj.speak())


animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())







# Lab
# 3: Multilevel
# Inheritance
# with Polymorphism
#     Create
#     Vehicle → Car → ElectricCar.
# Each
#
#
# class overrides the method fuel_type().
#
#
# Call
# the
# method
# using
# different
# object
# references.
#

class Vehicle:
    def fuel_type(self):
        return "Unknown"


class Car(Vehicle):
    def fuel_type(self):
        return "Petrol / Diesel"


class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"


v1 = Vehicle()
v2 = Car()
v3 = ElectricCar()

print(v1.fuel_type())
print(v2.fuel_type())
print(v3.fuel_type())







# Lab
# 4: Operator
# Overloading
# Create
# a
#
#
# class BankAccount with attribute balance.
#
#
# Overload + to
# add
# balances and > to
# compare
# balances.
# Demonstrate
# polymorphic
# behavior
# of
# operators.
#

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance


acc1 = BankAccount(5000)
acc2 = BankAccount(3000)

acc3 = acc1 + acc2
print(acc3.balance)

print(acc1 > acc2)







# Lab
# 6: Multiple
# Inheritance and MRO
# Create
# classes
# A, B, C, and D(diamond
# structure).
# Override
# the
# same
# method in B and C.
# Call
# method
# using
# D
# object and observe
# MRO.
#

class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


obj = D()
obj.show()

print(D.mro())





# Lab
# 7: Polymorphism
# with Exception Handling
# Create
# Calculator
#
#
# class with divide().
#
#
# Create
# SafeCalculator
# that
# overrides
# divide() and handles
# ZeroDivisionError.
# Demonstrate
# method
# overriding.

class Calculator:
    def divide(self, a, b):
        return a / b


class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"


calc: Calculator = SafeCalculator()

print(calc.divide(10, 2))
print(calc.divide(10, 0))




# Lab
# 8: Real - Time
# Payment
# System
# Create
# base
#
#
# class Payment with method pay().
#
#
# Create
# CreditCard, UPI, and NetBanking
# subclasses.
# Use
# a
# single
# function
# to
# process
# all
# payments

class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


def process_payment(payment_obj, amount):
    payment_obj.pay(amount)


process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(NetBanking(), 2000)
