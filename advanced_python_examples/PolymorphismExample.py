# Method overloading/constuvtor overloading is not possible in python/or constructor.No support at all.
# Method overriding is possible in python
class A:
    def m1(self, i):
        print(i, 'in class A m1')

    def m2(self, i):
        print(i, 'in class A m2')


class B(A):
    def m1(self, i):
        super().m1(10)#call super class method from child class
        print(i, 'in class B')


a = A()
a.m1(10)  # same method can be used for any kind of data ,No need of separate methods for different data

b = B()
b.m1(10)  # same class m1-->overriding
b.m2(20)  # parent class m2
