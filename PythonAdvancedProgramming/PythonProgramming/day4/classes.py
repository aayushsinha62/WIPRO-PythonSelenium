#class is a blueprint or a template
#which describes the state/behaviour of its object

class Student:
    #data or properties or attributes

    studentname="Ravi"
    studentID=67787


    #create function to access data
    #function indentation should be inside class
    #self is used to acess the attributes of class we have defined
    #self represents the instance of the class


    def displaystudentdetails(self):
        print(f"the student name is {self.studentname}")

#create object a of the class student
a=Student()
a.displaystudentdetails()

# write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects

class employee:
    emp_id=1
    emp_dept="CSE"

    def display(self):
        print(self.emp_id)
        print(self.emp_dept)

object=employee()
object.display()

