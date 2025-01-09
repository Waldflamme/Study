str = input('Введите строку заглавными буквами: ')
s = str.split( )
l = [0]*len(s)
for i in range(0,len(s)):
    l[i] = len(s[i])
print(min(l))