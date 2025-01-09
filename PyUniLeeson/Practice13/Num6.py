k = int(input('Enter k: '))
l = int(input('Enter l: '))

def Summing(a,b):
    if a>0 and b>0:
        print(a+b)
    else:
        raise AssertionError
Summing(k,l)