# functional programming is currently fashionable
from functools import reduce # not default part of latest Python 3
# map - we map one thing onto another thing

def square(x):
    return x*x
def add(x, y):
    return x + y
def isOdd(x):
    return x%2 != 0 # a filter function must return True or False
if __name__ == '__main__':
    sq_l = list( map( square, range(1,6) ) ) # take our map object and put all the results into a list
    print(sq_l)

    uppers = list( map( lambda s: s.upper(), 'python is cool'    ) )
    print(uppers)

    # filter members of a collection
    odds = list( filter(isOdd, range(0,10)) )
    print(odds)

    # reduce members from two collections by applying a function
    r = reduce( add, range(1,6), 10) # 25
    print(r)