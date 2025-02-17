a = int(input('Enter number: '))

def DivSelf(a):
    if a>0:
        print(f'SelfDiv = {a/a}')
    elif a==0:
        raise ValueError
DivSelf(a)