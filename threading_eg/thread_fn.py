from threading import Thread
import sys
import random
import time

def myfunc(n, max):
    for i in range(1,max):
        # print(n)
        sys.stdout.write(n) # prefer this for thread output
        time.sleep( random.random()*0.1 )

if __name__ == '__main__':
    thread1 = Thread(target=myfunc, args=('A',50) ) # a single member tuple needs the trailing comma
    thread2 = Thread(target=myfunc, args=('B',99) )
    # we need to explicitly start our threads
    thread1.start()
    thread2.start()
    # AND we need to join our threads
    thread1.join() # when the thread completes, it rejoins this main thread
    thread2.join()

    # otherwise the threads WILL join when our main thread completes