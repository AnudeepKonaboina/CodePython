# class for usage of self variable:
# self is used to declare instance variables of a class and to access them within a class .
# self is not a keyword in python .Any variable name can be used to represent self
# Self is the first variable by default in every method or class constructor.
# Self always points to the object of a class.
# The refrence values of self and refrence variables are always same
# PVM is responsible for passing the object refrence to self variable.

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(id(self))

    def add(self):
        print('Adiition of 2 numbers :', self.x, self.y, 'is ', self.x + self.y)
        self.z = 10

    def sub(a):  # any vaxriable can be used in the place of self.self is not a keyword ,so not mandatory
        print('sub of 2 numbers :', a.x, a.y, 'is ', a.x - a.y)


a = A(2, 3)
a.add()
print(id(a))
print(a.__dict__)
a.w = 10
print(a.__dict__)
