# Create
# a
# class Book with attributes title and author.
# Create
# 3
# different
# book
# objects and print
# all
# details.


class Book:

    def __init__(self, title, author):
            self.title=title
            self.author=author

    def display(self):
        print(self.title)
        print(self.author)

b1=Book("geeta","krishna")
b1.display()
b2=Book("ramayan","ram")
b2.display()
b3=Book("ram  charirtra manas","ram")
b3.display()


# Create
# a
#
#
# class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.

class Rectangle:

    def __init__(self, length, width):
        self.length=length
        self.width=width
        self.area=length*width
        self.perimeter=2*(length+width)

    def display(self):
        print(self.area)
        print(self.perimeter)

a1=Rectangle(10,20)
a1.display()

