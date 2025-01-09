str = input('Введите строку заглавными буквами: ')
l = 0
for i in range(0,len(str)):
    if 'А' in str[i]:
        l += 1
print (l)
