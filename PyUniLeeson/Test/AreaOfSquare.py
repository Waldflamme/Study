a = int(input('Enter a: '))
b = int(input('Enter b: '))

def Summing(a,b):
    if a>0 and b>0 and a==b:
        print(f'Area is: {a*b}')
    else:
        raise AssertionError
Summing(a,b)