from random import randint
def column(lst):
    col = []
    for j in range(len(lst[i])):
        col.append(lst[j][i])
    return col
def minus_el(lst):
    minus_lst = []
    c = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]<0:
                c+=1
        minus_lst.append(c)
        c = 0
    print()
    print(minus_lst)
    print()
    minus_el_ind = []
    for i in range(len(minus_lst)):
        minus_el_ind.append(i)
    print()
    print(minus_el_ind)
    print()
    max_el = max(minus_lst)
    min_el = min(minus_lst)
    ind_max = minus_lst.index(max_el)
    ind_min = minus_lst.index(min_el)
    minus_el_ind[ind_max] = ind_min
    minus_el_ind[ind_min] = ind_max
    return minus_el_ind
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
col_lst = []
for i in range(m):
    col_lst.append(column(a))
new_ord = tuple(minus_el(col_lst))
print()
print(new_ord)
print()
new_col_lst = []
for i in range(len(col_lst)):
    new_col_lst.append(col_lst[new_ord[i]])
print()
for i in range(m):
    for j in range(n):
        print(new_col_lst[j][i], end=' ')
    print()

lst = [[1,2],[2,3]]