# we can comprehensively iterate over a collection by using comprehensions
l = [5,4,3,2,1]

# [expression for item in iterable]
# here is a list comprehension - it returns a list by comprehensively iterating
my_numbers = [n*n for n in range(2, 99)]
print(my_numbers)
# here is a list comprehension that does logic
odd_l = [n for n in range(1, 99) if n%2 ==1]
print(odd_l)

# dictionary comprehension
# { key_expression : value_expression for expression in iterable}
word = 'letters' # a string
letter_counts = { letter:word.count(letter) for letter in word } # or set(word)
print(letter_counts)

# set comprehension
# { expression for expression in iterable }
my_set = { number*number for number in range(-9,9) if number%3 == 1 }
print(my_set)

# generator comprehension
# range is a generator - it generates the values without persisting them
# for i in range(3, 99, 4):
#     print(i)

# we can write our own generator
def my_range(first=0, last=10*100, step=1):
    number = first
    while number < last:
        # instead of a return statement, we have a yield statement
        yield number # yields the next value in the sequence being generated
        number += step

if __name__ == '__main__':
    print(my_range)
    inst = my_range()
    print(inst) # we have a generator object - remembers where we got to!!

# we can use our custom generator
    for x in inst:
        print(x)

    for x in inst: # the generator instance is exhausted, there are no more values to be yielded
        print('value is: {}'.format(x))

# we can explicitly call the 'next' member of a generator
    inst2 = my_range() # we have a fresh generator instance (it will yield values)
    print( inst2.__next__() ) # 0
    print( inst2.__next__() ) # 1
    print( inst2.__next__() )
    print( inst2.__next__() )
    # we can call the next members any time we like
    print( '{}, {}, {}'.format( inst2.__next__(), inst2.__next__(), inst2.__next__() ))