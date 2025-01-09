#7
num = int(input('Enter number of elements: '))
from random import randint
numbers = []
for i in range(0,num):
    numbers.append(randint(-999,999))
max_ind_1 = numbers.index(max(numbers))
max_ind_2 = numbers.index(max(numbers[:max_ind_1:]+numbers[max_ind_1+1::]))
min_ind_1 = numbers.index(min(numbers))
min_ind_2 = numbers.index(min(numbers[:min_ind_1:]+numbers[min_ind_1+1::]))
print(numbers)
print(f'Индекс 1 макс числ: {max_ind_1}\nИндекс 2 макс числ: {max_ind_2}')
print(f'1 макс числ: {numbers[max_ind_1]}\n2 макс числ: {numbers[max_ind_2]}')
print(f'Индекс 1 мин числ: {min_ind_1}\nИндекс 2 мин числ: {min_ind_2}')
print(f'1 мин числ: {numbers[min_ind_1]}\n2 мин числ: {numbers[min_ind_2]}')
if max_ind_1>max_ind_2:
    print(f'{numbers[max_ind_1]} {numbers[max_ind_2]}', end = ' ')
else:
    print(f'{numbers[max_ind_2]} {numbers[max_ind_1]}', end = ' ')
if min_ind_1>min_ind_2:
    print(f'{numbers[min_ind_1]} {numbers[min_ind_2]}', end = ' ')
else:
    print(f'{numbers[min_ind_2]} {numbers[min_ind_1]}', end = ' ')