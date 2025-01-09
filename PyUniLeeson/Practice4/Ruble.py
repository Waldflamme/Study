sum1 = int(input('Введите сумму: '))
if 1 <= sum1 < 999:
        if sum1%10 == 3 or sum1%10 == 2 or sum1%10 == 4:
                print(f'{sum1} рубля')
        elif sum1 < 10 and sum1%10 == 1:
                print(f'{sum1} рубль')
        elif sum1//100*100 + 20 < sum1 < (sum1//100 + 1)*100 and sum1%10 == 1:
                print(f'{sum1} рубль')
        else:
                print(f'{sum1} рублей')