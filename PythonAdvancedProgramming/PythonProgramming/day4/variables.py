# variables=used to store the data
#instance variables-global variables at class level
#local variables-inside the method only

#instance variables example
class student:

    school="St Joseph Convent"
    def __init__(self,name,marks): #local variables
        self.name=name  #instance variables or global
        self.marks=marks #instance variables or global #scope is throughout the class

    def show(self):
        schoolcity="Bangalore" #local or class variable #scope is inside method
        print(self.name, self.marks)
        print(schoolcity)
        print(self.school)

s1=student("aayush",99)
s2=student("harsha",90)
s1.show()
s2.show()

