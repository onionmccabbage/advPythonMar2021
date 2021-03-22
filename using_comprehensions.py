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
for i in range(3, 99, 4):
    print(i)
