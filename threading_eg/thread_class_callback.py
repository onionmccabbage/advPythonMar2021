from threading import Thread
import sys
import random
import time

class MyClass: # no need to extend the Thread class
    def __call__(self,*args): # ...but we MUST provide a __call__ method
        # act differently based on the number of args
        if len(args) == 0:
            pass
        if len(args) == 1:
            for i in range(1,50):
                sys.stdout.write(args[0])
                time.sleep(random.random()*0.1)
        if len(args) == 2:
            for i in range(1,args[1]):
                sys.stdout.write(args[0])
                time.sleep(random.random()*0.1)

if __name__ == '__main__':
    m1 = MyClass()
    # m2 = MyClass()
    # we can define a call-back instance which will be called by 'start'
    t1 = Thread(target= m1, args=('P',)) # call with one argument
    t2 = Thread(target= m1, args=('Q',99)) # deliberately use the SAME class
    t1.start()
    t2.start()
    t1.join()
    t2.join()


