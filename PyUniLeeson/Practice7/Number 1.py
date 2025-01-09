from random import randint
from copy import deepcopy
num = int(input('Enter number of elements: '))
lst_out = []
for i in range(num):
    lst_in = []
    lst_in.append(randint(1,9))
    for j in range(1,3):
        lst_in.append(randint(0,9))
    lst_out.append(lst_in)
lst_num = deepcopy(lst_out)
for i in range(num):
    for j in range(3):
        lst_num[i][j] = str(lst_num[i][j])
for i in range(num):
    lst_num[i] = ''.join(lst_num[i])
    lst_num[i] = int(lst_num[i])
print(lst_num)
lst_out = sorted(lst_out, key=sum)
for i in range(num):
    for j in range(3):
        lst_out[i][j] = str(lst_out[i][j])
for i in range(num):
    lst_out[i] = ''.join(lst_out[i])
    lst_out[i] = int(lst_out[i])
print(lst_out)
