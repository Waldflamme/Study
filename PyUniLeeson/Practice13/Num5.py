import math
n = int(input('Enter n: '))
n2 = float(input('Enter n: '))

def fact(num):
    if isinstance(num, int)  and num>0:
        print(math.factorial(num))
    else:
        print('Can'"'"'t find factorial for this number')
fact(n)
fact(n2)
