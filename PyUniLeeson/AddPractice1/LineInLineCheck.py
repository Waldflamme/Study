ln1 = str(input('Enter first sentence: '))
ln2 = str(input('Enter second sentence: '))
for symbol in ln1:
    if symbol in ln2:
        print('All elements of first sentence include all elements of second sentence')
    else:
        print('''First sentense doesn't include all elements of second''')
    break
