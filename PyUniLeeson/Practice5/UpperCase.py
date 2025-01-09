str_1 = input('Enter the line: ')
alf = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
quant = [0]
for i in range(0,len(str_1)):
    if str_1[i] in alf:
        quant.append(0)
print(len(quant) - 1)