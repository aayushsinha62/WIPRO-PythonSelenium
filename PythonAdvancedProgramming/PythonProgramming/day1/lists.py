from typing import ItemsView

empty_list=[]
numbers=[1,3,2,4]
mixeddata=[1,"hello",True,6.67,1]
nexted=[[1,2],[3,4]]

print(mixeddata[1])
print(mixeddata[2])

#modifying the data

mixeddata[4]=6
print(mixeddata)

#add elements #insert by index
mixeddata.insert(0,10)
print(mixeddata)

#append will add at te end
mixeddata.append("John")
print(mixeddata)

#remove elements
mixeddata.remove("hello")
print(mixeddata)

#list methods
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(2))
print(numbers.index(1))
print(numbers.clear())

fruits=["apple", "banana", "cherry"]
for item in fruits:
    print(item)

for i, fruit in enumerate(fruits):
    print(i,fruit)


#slicing

my_list=['p','a','r','r','o','t']
print("my_list=",my_list)
print(my_list[3:5])
print(my_list[3:])
print(my_list[:])

#extends adding elements of one list to another

numbers=[1,2,3]
nextnumber=[5,6,7]

numbers.extend(nextnumber)
print(numbers)