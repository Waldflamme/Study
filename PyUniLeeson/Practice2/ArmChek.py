num = int(input('Enter a 3-digit number:'))
x = num%10
y = (num%100-num%10)/10
z = num//100
if x**3+y**3+z**3==num:
    print('This is armstrong')
