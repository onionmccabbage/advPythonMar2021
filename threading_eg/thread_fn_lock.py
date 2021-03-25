import threading
import time
import random
import sys

# you can try this code with the locks and also comment out the locks....

# we can declare a global variable
counter = 1 # it is not in a block, so it is global (to this module)
lock = threading.Lock()

# declare some functions which will be invoked by threads
def workerA():
    global counter # we now have acces to the global variable inside this function
    lock.acquire()
    try:
        # count to ten, and increment the counter
        while counter <10:
            counter += 1
            sys.stdout.write('Worker A is incrementing counter to {}\n'.format(counter))
            time.sleep(random.randint(0,1)) # a random sleep between 0 and 1 second
    finally:
        pass
        lock.release()

def workerB():
    global counter # we now have acces to the global variable inside this function
    lock.acquire()
    try:
        # count to minus ten, and decrement the counter
        while counter >-10:
            counter -= 1
            sys.stdout.write('Worker B is decrementing counter to {}\n'.format(counter))
            time.sleep(random.randint(0,1)) # a random sleep between 0 and 1 second
    finally:
        pass
        lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)

    t2.start()
    t1.start()

    t1.join()
    t2.join()
