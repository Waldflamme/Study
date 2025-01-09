from random import randint
def column(lst):
    col = []
    for j in range(len(lst[i])):
        col.append(lst[j][i])
    return col
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
rev_mat = []
for i in range(n):
    rev_mat.append(column(a))
min_el = []
for i in range(m):
    min_el.append(min(rev_mat[i]))
for i in range(n):
    a[i].append(rev_mat[min_el.index(min(min_el))][i])
print(rev_mat[min_el.index(min(min_el))])
print()
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()