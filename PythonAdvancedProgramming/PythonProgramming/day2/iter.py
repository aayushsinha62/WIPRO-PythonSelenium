#iter() method - built in method that allows to create a iterator
#create a iterator from a iterable
#iteration - looping in collection of items

a=[10,30,30,40,50]

#convert list into iterator

iterator=iter(a)

#next() allow the user to acess the elements

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#string to iterator

s="hello"
iterator=iter(s)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#dictionary to iterator

d={'a':1,'b':2, 'c':3}
iterator=iter(d)
print(next(iterator))
print(next(iterator))


#for loop to iterate

for key in iterator:
    print(key)

d={'a':1, 'b':2, 'c':3}
for key,value in d.items():
    print(key,"->", value)

#iter(callable, sentinel)

def get_input():
    return input("Enter value:")

for value in iter(get_input, "quit"):
    print("Your entered", value)

print("loop ended")

