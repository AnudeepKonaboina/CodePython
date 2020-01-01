# Static or class variables
# variable whose value doesnt change from object to object rather only one copy is maintained .
# 1.declared within  a class directly 2.within a instance method and a constructor using classname 3.within clssmethod using cls and classname 4.within static method using classname 5.outside class using classname
# 2.Access  1.within constuctor using self,class name  2.within a method using self,classname3.within a classmethod using cls,classname 4.Inside staticmethod using classname5.outside class using classname or ref variable
# del can e done uing classname in all the cases.
class B:
    cname = 'MGIT'  # directly

    def __init__(self):
        B.cadd = 'Hyd'  # using class name

        print(B.cname)
        print(self.cname)
        print(B.cadd)

    def m1(self):
        B.cpri = 'Babu'  # using class name
        print(B.cname)
        print(self.cname)

    @classmethod
    def m2(cls):
        cls.cvp = 'ddd'  # using cls
        B.cvvp = 'aaa'  # using classname
        print(B.cname)
        print(cls.cname)
        print(cls.cvp)

    @staticmethod
    def m3():
        B.cxx = 'eee'  # using class name
        print(B.cname)
        print(B.cvp)


B.ooc = 'kkk'
b = B()
print(b.cname)
print(B.__dict__)
b.m1()
print(B.__dict__)
