# operator polymorphism means
# the same operator behaves differently for diff data types or the objects
# add numbers
# + joins the strings
# + merges the lists
# # operator overloading in python
from multiprocessing.util import log_to_stderr

# __add__()
# __sub__()
# __mul__()
# __eq__()
# __lt__()
# __gt__()

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # + operator
    def __add__(self, other):
        return self.name + other.name

    # - operator
    def __sub__(self, other):
        return self.marks - other.marks

    # * operator
    def __mul__(self, other):
        return self.name * other.marks

    # == operator
    def __eq__(self, other):
        return self.marks == other.marks

    # < operator
    def __lt__(self, other):
        return self.name < other.marks

    # > operator
    def __gt__(self, other):
        return self.marks > other.marks


# objects
s1 = Student("Aayush", 80)
s2 = Student("Rahul", 70)

# using operators
print("Addition:", s1 + s2)
print("Subtraction:", s1 - s2)
print("Multiplication:", s1 * s2)
print("Equal:", s1 == s2)
print("Less than:", s1 < s2)
print("Greater than:", s1 > s2)
