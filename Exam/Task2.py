import math

n = int(input('Enter n: '))
m= int(input('Enter m: '))

def func1(n,m):
    l = math.gcd(m,n)
    st = (int(n/l),int(m/l))
    print(st)

def func2(lst):
    l = math.gcd(m,n)
    ls = []
    for i in lst:
        ls.append(int(i/l))
    print(ls)

func1(n,m)

lst = [n,m]
func2(lst)