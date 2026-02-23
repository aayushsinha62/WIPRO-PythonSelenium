class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
class D(B,C):
    def show(self):
        print("Class D")
d=D()
d.show()
print(D.mro())
#methods fromm left to right