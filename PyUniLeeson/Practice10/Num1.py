a = int(input('Enter a: '))
h = int(input('Enter h: '))
def TriangleP(a,h):
    p=(((a*0.5)**2+h**2)**0.5)*2+a
    return p
print(f'Perimetr is: {TriangleP(a,h)}')