str_1 = input('Enter a line: ')
num = int(input('Enter a number: '))
lst = list(str_1)
for i in range(0,(len(lst)-1)):
    print(f'{lst[i]}{"#"*num}', end = '')
print(lst[-1])