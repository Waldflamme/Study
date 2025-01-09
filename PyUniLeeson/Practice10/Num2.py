num = input('Enter a number: ')
def InvertDigits(num):
    ls = []
    for i in range(len(num)):
        ls.append(num[i])
    ls_rev = list(reversed(ls))
    for i in range(0,len(ls_rev)):
        print(ls_rev[i], end = '')
InvertDigits(num)