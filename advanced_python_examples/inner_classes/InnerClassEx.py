# inner classes demo
class A:
    class B:
        pass

    class C:
        def m1(self):
            print("in method m1 in C class")


ref = A()
ref2 = ref.C()
ref2.m1()  # access inner class method
