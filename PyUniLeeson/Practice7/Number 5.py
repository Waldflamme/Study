from random import randint
def min_in_row(lst):
    lst1 = []
    for i in range(len(lst)):
        lst1.append(min(lst[i]))
    return lst1.index(min(lst1))
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))
a = []
b = []
for i in range(n):
    for j in range(m):
        b.append(randint(-999,999))
    a.append(list(b))
    b.clear()
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()
print()
c = []
for i in range(n):
    if i == min_in_row(a):
        c.append([0]*m)
        c.append(a[min_in_row(a)])
    else:
        c.append(a[i])
for i in range(len(c)):
    for j in range(m):
        print(c[i][j], end = ' ')
    print()