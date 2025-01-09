ln1 = list(map(str, input('Enter 3 word long sentence: ').split()))
if len(ln1)>3:
    print('The sentence is longer than 3 words')
elif len(ln1)<3:
    print('The sentence is shorter then 3 words')
else:
    print(*ln1[::-1])
# list(map('type', input().split())) - для ввода списка в виде строки
# print(*'variable'[::-1]) - вывод строки, определенной в параметре, в обратном порядке
