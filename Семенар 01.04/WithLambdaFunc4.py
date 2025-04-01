import random
from functools import reduce

num = [random.randint(1, 50) for i in range(10)]
print(num)

odd = list(filter(lambda x: x % 2 != 0, num))

odd_sort = sorted(odd, reverse=True)
print(odd_sort)

product = reduce(lambda x, y: x * y, odd_sort, 1)
print(product)
