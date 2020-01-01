# when the program is terminated Garbage collector will be activated and will call the del method before termination
from time import *


class A:
    def __init__(self):
        print("object creating")

    def __del__(self):
        print("object destroying")


a = A()
a = None  # assign nune value .then the object is eligible for garbage collection.
del a  # using del function
sleep(3)
print("End")
