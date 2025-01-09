from random import randint
def column(lst):
    col = []
    for j in range(len(lst[i])):
        col.append(lst[j][i])
    return col
def max_min_change(lst):
    max_el = max(lst)
    min_el = min(lst)
    ind_max = lst.index(max_el)
    ind_min = lst.index(min_el)
    lst[ind_max] = int(min_el)
    lst[ind_min] = int(max_el)
    return lst
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
    rev_mat.append(max_min_change(column(a)))
for i in range(m):
    for j in range(n):
        print(rev_mat[j][i], end=' ')
    print()