# Instance Variables of a class
# If the value of a variable changes from one instance to another instance ,then it is a instance varaible.
# declared 1.inside const using self 2.inside method using self 3.outside class using ref variable
# accessed 1.inside method and constructor using self 2.outside class using refrence variable
# cannot declare or access instance variables using claas and static method
# 'del' keyword is used to delete instance variables.

class A:
    def __init__(self):
        self.a = 10  # declared
        self.b = 20
        self.c = 30
        del self.c
        print(self.a)  # accessed

    def m1(self):
        self.d = 40  # declared
        del self.d  # deleition using del
        print(self.a)
        print(self.b)
        print(self.c)  # accessed


a = A()
a.e = 50
del a.e
print(a.b)
print(a.__dict__)  # gives the dict containing the instance variables of a class
