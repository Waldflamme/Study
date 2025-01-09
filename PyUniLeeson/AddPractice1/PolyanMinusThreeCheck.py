line = str(input('Enter line:'))
if line[2:len(line):1] == line[len(line):2:-1]:
    print('This is polyandrom')
else:
    print('This is not polyandrom')