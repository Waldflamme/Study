str1 = input('Enter line: ')
for i in range(0,len(str1)):
    if str1[i] != ' ':
        print(chr(ord(str1[i])+1), end = '')
    else:
        print(' ', end = '')