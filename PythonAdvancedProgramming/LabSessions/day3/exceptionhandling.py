# 2.write a program to handle invalid user input

try:
    num=int(input("enter an integer"))

except ValueError:
    print("invalid number")


# 3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

char=random.choice(string.ascii_letters)
print(char)


length=random.randint(2,5)
result=""

for i in range(length):
    result += random.choice(string.ascii_letters)

print(result)


length=int(input("enter fixed length"))
result=""

for i in range(length):
    result += random.choice(string.ascii_letters)

print(result)