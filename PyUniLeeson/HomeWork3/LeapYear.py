year = int(input('Enter the year: '))
if year%400==0 or year%4==0:
    print('This is a leap year')
else:
    print('This is not a leap year')