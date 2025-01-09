num1 = float(input('Enter firsrt num: '))
num2 = float(input('Enter second num: '))
oper = str(input('Enter operation "+-*/": '))
if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
elif oper=='/' and num2==0:
    print ('Can'"'"'t divide by 0')
else:
    print(num1/num2)