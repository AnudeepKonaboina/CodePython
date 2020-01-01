# There are three  types of methods
# 1.instance method-->used for dealing with object level data
# 2.classmethod -->used for accessing class level data-using cls
# 3.static method-->helper or utility method


class A:
    def m1(self):
        print("instance method")

    @classmethod
    def m2(cls):
        print("class method")

    @staticmethod
    def m3():
        print("static method")


a = A()
a.m1()  # access using object refrence
A.m1(a)  # access using class name with ref val a as param as it becomes a static method when instance method is called using class name.

# access class method using object ref and calss name
a.m2()
A.m2()

# access static method using classname and object ref.best parctice is class name
a.m3()
A.m3()
