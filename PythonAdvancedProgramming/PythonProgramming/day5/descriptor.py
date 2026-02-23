#descriptor - control the access of the object atttributes

#__get__()
#__set__()
#__delete__()

class Desc:
    def __get__(self,instance,owner):
        print("getting the value")
        return 10

class Test:
    x=Desc()

t=Test()
print(t.x)

#this non-data descriptor uses only __get__ descriptor
#data desc uses both get and set method

class mydesc:
    def __get__(self,instance,owner):
        return instance._value

    def __set__(self,instance,value):
        print("setting the value")
        instance._value=value

class Test:
    x=mydesc()

t=Test()
t.x=100
print(t.x)


#using __del__

class Name:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        print("setting the value")
        instance._value = value

    def __del__(self,instance):
        print("deleting name")
        del instance._name


class Person:
    name=Name()

p=Person()
p.name="Aayush"
del p.name



t = Test()
t.x = 100
print(t.x)