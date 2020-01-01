# sample program for class declaration and use of a class

class Employee:
    def __init__(self, eno, ename, esal):
        # __init__ is the constructor in python.Mandatory syntax
        # used for initializing the instance variables of a class.
        # It is executed as and when an object is created.
        # It is executed only once per program execution
        # there can ony be one constructor in python .No overloading of constructor but overriding is the concept.Latest constuctor declared in the final constuctor.
        # There is no constructor overloading,method overloading ,but there is only operator overloading.
        print('class constructor called ')
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def displayDetails(self):
        # method of a class
        print("number   :", self.eno)
        print("name     :", self.ename)
        print("Salary   :", self.esal)


a = Employee(1, 'a', 1000)
a.displayDetails()
print(a)  # refrence value internally calls a.__str__()
print(id(a))  # id value of the object
print(hex(id(a)))  # ref value
print(Employee.__dict__)  # lit of all the variables declared
print(a.__dict__)  # dict of instance varaiables
print(a.__str__())  # refrence value

b = Employee(2, 'a', 2000)
b.displayDetails()
print(id(b))
