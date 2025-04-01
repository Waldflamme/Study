import random
from functools import reduce

num = [random.randint(1, 50) for i in range(10)]
print(num)

filtered_num = list(filter(lambda x: x < 15, num))

sort_num = sorted(filtered_num, reverse=True)
print(sort_num)

sum_result = reduce(lambda x, y: x + y, sort_num, 0)
print(sum_result)
