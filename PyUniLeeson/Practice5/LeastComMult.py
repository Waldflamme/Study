#2
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
max_num = max([num1,num2])
max_div = []
for i in range(1,max_num):
    if num1%i==0 and num2%i==0:
        max_div.append(i)
max_div_num = max(max_div)
print('НОК: ',abs(num1*num2)/max_div_num)