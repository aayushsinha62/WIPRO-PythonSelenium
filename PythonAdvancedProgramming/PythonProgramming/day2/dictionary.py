#dictionary items - key value  pairs
#similar to list and tuples
#dictionary itself is mutable
#key should always be immutable
#values can be mutable or immutable
#for integers, tuples and strings - keys are immutable but tuple shouldnt have list inside
# list, set cant be used as keys as they are mutable
#list cannot be used in key for the dictionary as it is mutable in nature

country={
    "India":"Delhi",
    "Canada":"Ottawa",
    "England":"London"

}

print(country)

#access values with the keys
print(country["Canada"])

#add elements

country["Italy"]="Rome"
print(country)

#deleting elements

del country["India"]
print(country)

#clear
#country.clear()

#iterate among the dictionary
for coun in country:
    print(coun)

#for length of dictionary
print(len(country))

#pop - removes the item with spec key

x=country.pop("Canada")
print(x)

#update() adds or changes the dictionary

country.update({"age":23, "city":"bangalore"})
print(country)

#keys() returns all keys in dictionary

print(country.keys())

#values() returns all values in dictionary

print(country.values())

#popitem() returns the last inserted keyword

x=country.popitem()
print(country)

#copy returns the copy of dictionary

new_country=country.copy()
print(new_country)

#dictionary inside the list

employees=({"id":1, "name":"harsha","role":"QA"},
           {"id":2, "name":"aayush","role":"dev"},
           {"id":3, "name":"ravi","role":"manager"})
print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"], emp["role"])

employees.append({"id":4, "name":"Sita", "role":"tester"})
print(employees)

employees.pop(0)
print(employees)

#search in item in the list

for emp in employees:
    if emp["name"]=="Harsha":
        print(emp)

#integer is a key for int keys must be immutable

my_dict={1:"one",2:"two", 3:"three"}
print(my_dict)

#tuples as a key

my_dict={(1,2):"One Two",3:"Three"}
print(my_dict)

my_dict={(1,2):"One Two",3:"Three"}
print(my_dict)

my_dict={(1,2):"One Two",3:"Three", 3:"four"}
print(my_dict)

#list as key

#my_dict={1:"Hello", [1,2]:"There you"}
#print(my_dict)

#not allowed so error




