mylist = [1,7,11,42]

# create an iterable
list_iter = iter(mylist)

print( list_iter.__next__() )
print( list_iter.__next__() )
print( list_iter.__next__() )

rev_iter = reversed(mylist)

print( rev_iter.__next__() )
print( rev_iter.__next__() )
print( rev_iter.__next__() )

# we can iterate over a file
f = open('stuff.txt') # default is read from text
for line in f:
    print(line, end='') # we can customize the line-end character

# we can declare our own class and make it iterable
class Evens:
    def __init__(self, limit):
        self.__limit = limit
        self.__val = 0
    # we must override __iter__ and __next__
    def __iter__(self):
        return self
    def __next__(self):
        if self.__val > self.__limit:
            raise StopIteration # we MUST raise StopIteration if we exceed the iterable members
        else:
            return_val = self.__val
            self.__val +=2
        return return_val

for i in Evens(6):
    print(i)  

inst = Evens(2)
print(inst.__next__())
print(inst.__next__())  
print(inst.__next__())  # this raises our StopIteration exception

