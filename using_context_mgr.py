# in Python 3 we have a 'context manager'
from contextlib import contextmanager
import sys

@contextmanager
def stdout_redirect(new_std):
    save_stdout = sys.stdout
    sys.stdout = new_std
    yield # the function will yield the next available object to we written
    sys.stdout = save_stdout # reset to normal stdout

if __name__ == '__main__':
    with open('mylog.txt', 'a') as fobj: # 'w' overwrite, 'a' append 'x' exclusive
        with stdout_redirect(fobj):
            print('this will be redirected to our log file')
    print('both "with" operators have ended, so we\'re back to normal stdout')