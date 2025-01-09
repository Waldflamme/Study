num = int(input('Enter number of elements: '))
from random import randint
numbers = []
for i in range(0,num):
    numbers.append(randint(-999,999))
new_numbers = []
for j in range(0,num):
    if numbers[j]%2==0:
        new_numbers.append(numbers[j])
rev_numbers = numbers[::-1]
for l in range(0,num):
    if rev_numbers[l]%2==1:
        new_numbers.append(rev_numbers[l])
print(numbers)
print(new_numbers)