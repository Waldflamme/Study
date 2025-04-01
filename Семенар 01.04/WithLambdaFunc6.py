import random
from functools import reduce

num = [random.randint(1, 50) for i in range(10)]
print(num)

even_index_num = list(filter(lambda x: num.index(x) % 2 == 0, num))

sorted_num = sorted(even_index_num)
print(sorted_num)

sum_result = reduce(lambda x, y: x + y, sorted_num, 0)
print(sum_result)
