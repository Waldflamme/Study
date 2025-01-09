str_1 = input('Введите строку буквами: ')
str_2 = input('Введите строку буквами: ')
st_1 = list(str_1)
st_2 = list(str_2)
s = st_1[0]
v = st_2[0]
st_1[0] = v
st_2[0] = s
st_1.append(' ')
n = (st_1 + st_2)
f = ''.join(n)
print(f)
