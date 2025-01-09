a = int(input('Enter first num: '))
b = int(input('Enter sec num: '))
h = int(input('Enter step num: '))
for i in range(a,b,h):
    print((a + h)**2)
    a+=h
