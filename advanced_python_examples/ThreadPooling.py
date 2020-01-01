from concurrent.futures import ThreadPoolExecutor

from threading import *


class MultiThread:
    def main(self):
        executor = ThreadPoolExecutor(max_workers=3)
        executor.submit(self.m1(1))
        executor.submit(self.m1(3))
        executor.submit(self.m1(4))

    def m1(self, number):
        print(current_thread().getName(), number, 'is executing')


print(current_thread().getName())

if __name__ == '__main__':
    mt = MultiThread()
    mt.main()
