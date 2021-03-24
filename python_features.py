# zip (nothing to do with compressing archives)
days = ['Mon', 'Tue', 'Wed']
fruits = ('banana', 'orange', 'kiwi')
drinks = ['coffee', 'tea', 'water']
desserts = ['tiramasu', 'ice cream', 'pie', 'pudding'] # 4 members! 

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print('{} drink {} with {} followed by {}'.format( day, drink, fruit, dessert ))

# named tuple
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
d = Duck('wide orange', 'long')
print(d)