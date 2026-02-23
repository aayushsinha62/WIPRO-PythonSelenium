#multiple inheritance - single base class is derived from multiple parent class
class Parent1:
    pass

class Parent2:
    pass

class child(Parent1,Parent2):
    pass
class Father:
    def driving(self):
        print("Father has the skill to drive")
class Mother:
    def cooking(self):
        print("Mother has skills to cook")
class Child(Father,Mother):
    def both_skills(self):
        print("Child has skills to study")
        print("Child has both skills of driving and cooking")
c=Child()
c.cooking()
c.driving()
c.both_skills()