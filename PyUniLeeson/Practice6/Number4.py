#4
len_lst = int(input('Enter list length: '))
from random import randint
numbers = []
for i in range(0,len_lst):
    numbers.append(randint(0,999))
digit2num = []
for j in range(len_lst):
    if 9<numbers[j]<100:
        digit2num.append(numbers[j])
print(numbers)
print(sorted(digit2num))