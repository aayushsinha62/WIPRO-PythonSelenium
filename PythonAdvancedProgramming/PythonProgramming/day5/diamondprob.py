class A:
    def show(self):
        print("Class A")

class B(A):
    # pass
    def show(self):
        print("Class B")

class C(A):
    #pass
    def show(self):
        print("Class C")

class D(B,C):
    #pass
        print("Class D")

d=D()
d.show()
print(D.mro())
#methods fromm left to right

#DBCA


class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
        super().show()
class C(A):
    def show(self):
        print("Class C")
        super().show()
class D(B,C):
    def show(self):
        print("Class D")
        super().show()
d=D()
d.show()
print(D.mro())
#methods fromm left to right