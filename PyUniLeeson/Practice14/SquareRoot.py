a = int(input('Enter number: '))

def SquareRoot(a):
    if a>=0:
        print(f'SquareRoot = {a**0.5}')
    elif a<0:
        raise ValueError
SquareRoot(a)