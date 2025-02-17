from random import randint
K = int(input('Enter K: '))-1
L = int(input('Enter L: '))-1
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))


def RemoveRowCol(lst):
    if K <= n and L <= m:
        c = []
        for i in range(n):
            if i==K:
                continue
            d = []
            for j in range(m):
                if j==L:
                    continue
                d.append(lst[i][j])
            c.append(d)
        return c
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
ls = RemoveRowCol(a)
for i in ls:
    for j in i:
        print(j, end = ' ')
    print()