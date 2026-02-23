#default methods - built in methods,
#user defined methods - method name, method body

#parameterised methods
#it allows the same method to behave differently for diff inputs

class Calculator:
    def add(self,a,b):
        print(a+b)

c=Calculator()
c.add(10,20)
c.add(20,25)

#default parameters

class Test:
    def run(self,browser="chrome"):
        print("running on",browser)

t=Test()
t.run()
t.run("Firefox")

#*args parametereized methods

class Numbers:
    def total(self,*args):
        print(sum(args))

n=Numbers()
n.total(10,20,30)
n.total(10)
n.total(20,30)