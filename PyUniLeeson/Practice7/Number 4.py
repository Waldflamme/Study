from random import randint
def column(lst):
    col = []
    for j in range(len(lst[i])):
        col.append(lst[j][i])
    return col
def av_sum(lst1):
    c = 0
    for i in range(len(lst1)):
        if lst1[i]>sum(lst1)/len(lst1):
            c+=1
    return c
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))
a = []
b = []
for i in range(n):
    for j in range(m):
        b.append(randint(0,999))
    a.append(list(b))
    b.clear()
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
print()
for i in range(n):
    print(column(a))
    print(av_sum(column(a)))
    print()