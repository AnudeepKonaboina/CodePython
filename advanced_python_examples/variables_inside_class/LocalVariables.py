# local variables 1.declared inside a method or within contuctor paranthesis
#scope is within the method or condtructor boddy
# can be accessed within method and not outside the method,to access we must declare it as global
class C:
    a=10
    def __init__(self,a):
        a=10
        self.a=a
        print(a)


c = C(1)
print(c.a)


