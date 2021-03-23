# using the context manager
import sys

class Redirect:
    ''' provide a way to redirect the standard output'''
    def __init__(self, new_stdout):
        '''Receive a new stdout '''
        self.new_stdout = new_stdout
    # we override __enter__ and __exit__
    def __enter__(self):
        '''Implement redirect'''
        self.save_stdout = sys.stdout
        sys.stdout = self.new_stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''Restore original stdout '''
        sys.stdout = self.save_stdout

if __name__ == '__main__':
    # fout = open('mylog.txt')
    # print('here is some text', file=fout)
    # use our Redirect class
    with open('mylog.txt', 'w') as fobj: # the 'with' operator makes use of an object and closes it when done
        with Redirect(fobj):
            print('this gets printed into our log file')
    print('this prints to the console')
    # print(sys.stdout, sys.stdin)
    # print(sys.float_info)
    # print(sys.maxsize)
    # print(sys.path)
