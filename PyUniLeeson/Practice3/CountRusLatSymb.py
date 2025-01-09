str = input('Введите строку заглавными буквами: ')
rus = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
lat = 'abcdefghigklmnopqrstuvwxyz'
l = [0]
for i in range(0,len(str)):
    if str[i] in rus:
        l.append(0)
    elif str[i] in lat:
        l.append(0)
print(len(l)-1)
