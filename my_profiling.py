# to profile this module:
# python -m cProfile -o profiling_output my_profiling.py
# declare some methods to be profiled

from functools import reduce

def fib(n): 
    sequence = (0,1)
    for _ in range(2, n+1):
        sequence += (reduce(lambda a, b: a+b, sequence[-2:]),)
    return sequence[n]

def count(): # everything is an object
    count.num_calls += 1 # a property attached to a method!!
    print(count.num_calls)

if __name__ == '__main__':
    count.num_calls = 0
    # call our methods
    print(fib(25))
    # and...
    for _ in range(1, 20):
        count()