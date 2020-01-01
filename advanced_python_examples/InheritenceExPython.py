# inheritance -->inheriting the parent methods and constructors and varibles in child class is called inheritance.
class Parent:
    def __init__(self):
        print("calling constructor")
        self.a = 10
        self.b = 20

    def m1(self):
        print("parent method m1")


class Child(Parent):
    pass


c = Child()  # child object
c.m1()  # accessing parent method
print(c.a)  # accessing parent variables
print(c.b)
c.__init__()  # accessing parent constructor using child object
