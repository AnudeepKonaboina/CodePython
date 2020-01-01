# Multithreadding-used for running independent jobs or tasks parallelly ,so that performance is improved and the time is saved.
# There are three ways to create a thread in python
# 1.Without using any class
# with extending  Thread class
# without extending thread class

# Example of multi threaded programming 1sat way without using a class
from threading import *


def m1():
    for i in range(10):
        print(current_thread().getName(), '\n')


t = Thread(target=m1)
t.start()
for i in range(10):
    print(current_thread().getName(), '\n')

# ======================================================================================#
# second way by extending thread class
from threading import *
from time import *


class A(Thread):
    def run(self) -> None:
        for i in range(10):
            sleep(10)
            print(current_thread().getName())


a = A()
a.start()
for i in range(10):
    sleep(5)
    print(current_thread().getName(), '\n')
# ===================================================================================#
# without using extends
from threading import *
from time import *


class A:
    def m1(self):
        for i in range(10):
            sleep(10)
            print(current_thread().getName())


a = A()
t = Thread(target=a.m1)
t.start()
for i in range(10):
    sleep(5)
    print(current_thread().getName(), '\n')
