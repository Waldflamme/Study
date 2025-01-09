#5
len_lst = int(input('Enter list length: '))
from random import randint
numbers = []
for i in range(0,len_lst):
    numbers.append(randint(1,2))
l1 = set(numbers)
print(numbers)
print(tuple(l1))
