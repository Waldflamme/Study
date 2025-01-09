ln1 = int(input('Enter 4-digit number: '))
x = ln1%10
y = ln1%100-ln1%10
z = ln1%1000-ln1%100
v = ln1//1000
if x==7 or y==7 or z==7 or v==7:
    print('This num contains 7')