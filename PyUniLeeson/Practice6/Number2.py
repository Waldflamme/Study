#2
len_lst = int(input('Enter list length: '))
from random import randint
numbers = []
for i in range(0,len_lst):
    numbers.append(randint(-999,999))
numbers_1 = []
for j in range(len_lst):
    if numbers[j]<0:
        numbers_1.append(numbers[j])
for l in range(len_lst):
    if numbers[l]>0:
        numbers_1.append(numbers[l])
print(numbers)
print(numbers_1)