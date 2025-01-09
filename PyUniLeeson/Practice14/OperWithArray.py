from random import randint
m = int(input('Enter number of columns: '))
n = int(input('Enter number of strings: '))


def ArraySumEven(lst):
    if m==n:
        ls = []
        for i in range(n):
            for j in range(i+1,len(lst[i])):
                ls.append(lst[i][j])
        print(ls)
        print(f'Arithmetic mean: {sum(ls)/len(ls)}')
        ls1 = []
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if i>j and lst[i][j]%2==0:
                    ls1.append(lst[i][j])
        print(ls1)
        print(f'Number of evens: {len(ls1)}')
    else:
        raise AssertionError
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
ArraySumEven(a)