num = int(input('Enter a number: '))
num_l = [0]*num
for i in range(1,num):
    if num%i == 0:
        num_l[i] = i
if sum(num_l) == num:
    print('This is a perfect number')
else:
    print('This is not a perfect number')