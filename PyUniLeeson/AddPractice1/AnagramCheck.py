ln1 = list(map(str, input('Enter first sentence: ')))
ln2 = list(map(str, input('Enter second sentence: ')))
ln1.sort()
ln2.sort()
if ln1==ln2:
    print('This is an anagram')
else:
    print('This is not an anagram')