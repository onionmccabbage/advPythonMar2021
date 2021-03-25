from threading import Lock
import sys
import random
import time

def main():
    lock = Lock() # create a lock instance
    lock.acquire() # give THIS thread access to the lock
    try:
        for i in range(1, 50):
            sys.stdout.write('{}'.format(i))
            time.sleep(random.random()*0.1)
    finally:
        lock.release() # make sure we let go of the lock! (so other threads can use it)

if __name__ == '__main__':
    main() # this is a common syntax