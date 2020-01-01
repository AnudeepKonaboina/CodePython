# Inheriting the properties of the parent into the class is the process of inheritance.Code reusability is the major adv.of inheritance.
#  There are  types of inheritance
# 1.Single level inheritance--one child one parent(p-c)
# 2.Multilevel inheritance--(p-c-p-c...)
# 3.Multiple inheritance--single child multiple parents(p1-c,p2-c) .uses MRO algorithm for getting the right order of method.
# 4.Hierarchical inheritance--single parent multiple childs(p-c1,p-c2)
# 5.Cyclic Inheritance--(p-p-p)
# 6.Hybrid inheritance--combination of all 4 inheritances

class Parent:
    def __init__(self):
        self.x = 0

    def m1(self):
        print('m1 in parent')


class Child:
    def __init__(self):
        self.y = 1

    def m1(self):
        print('m1 in child')


class SubChild(Parent, Child):
    def __init__(self):
        self.z = 10


def main():
    child = Child()
    print(child.m1())


main()
print(Parent.__dict__)
print(SubChild.mro())

subchild = SubChild()
subchild.m1()
