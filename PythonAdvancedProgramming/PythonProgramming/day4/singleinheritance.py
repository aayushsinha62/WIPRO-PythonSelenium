#single inheritance
#parent --> child class - properties from parent class are acquired to child class
#create the object of child classes to bring inheritance to picture


#parent class
class employee:
    def __init__(self, name,empid):
        self.name=name
        self.empid=empid

    def empdetails(self):
        print(self.name,self.empid)

#child class

class Manager(employee):

    def approve_leave(self):
        print("leave approved")

m=Manager("John",7878) #even though manager doesnt have constructor it calls employee init automatically thats single inheritance
m.empdetails() #from parent class
m.approve_leave() #from child class