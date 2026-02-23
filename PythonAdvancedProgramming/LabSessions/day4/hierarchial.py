#hierarchial inheritance

class Employee:

    def login(self):
        print("Employee is logged in")

class Developer(Employee):

    def write_code(self):
        print("writing code")

class Tester(Employee):

    def test_app(self):
        print("test the application")

dev=Developer() #child1
test=Tester() #child2