# Create a dictionary with student roll number as key and name as value. Print the dictionary.
# Access the value of a key that exists and one that does not exist
# Update the value of an existing key in a dictionary.
# Delete a key from a dictionary using:
# del
# pop()
# Find the number of key–value pairs in a dictionary.
# Print only:
# keys
# values
# key–value pairs

students= {101:"aayush",
         102:"aadarsh",
         103:"aaditya"}

print(students)

#accessing present key
print(students[101])

#accessing non present key
print(students.get(105))

#update
students[102]="sana"
print(students)

#using delete
del students[103]
print(students)

#using pop
students.pop(101)
print(students)

#number of key value pairs
print(len(students))

#printing only keys
print(students.keys())

#printing only values
print(students.values())

#printing key-value pairs
print(students.items())















