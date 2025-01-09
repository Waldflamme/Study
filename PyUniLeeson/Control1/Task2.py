from random import randint
n = int(input('Enter n: '))
L3 = []
for i in range(2*n+1):
    L3.append(randint(-999,999))
L_mid = sorted(L3)
print(L3)
print(L_mid[n])