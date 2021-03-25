from threading import Thread
import sys
import random
import time

class MyClass(Thread): # we extend the Thread class
    def __init__(self, n):
        Thread.__init__(self) # call the __init__ method of the parent class
        self.n = n
    # for Threads, we can override the 'run' method
    def run(self):
        for i in range(1,50):
            sys.stdout.write(self.n)
            time.sleep(random.random()*0.1)

if __name__ == '__main__':
    m1 = MyClass('X')
    m2 = MyClass('Y')
    m1.start()
    m2.start()
    m1.join()
    m2.join()


