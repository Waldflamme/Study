a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

def DivNum(a,b):
    if a>0 and b>0:
        print(f'a/b = {a/b}')
    elif a>0 and b==0:
        raise ZeroDivisionError
DivNum(a,b)