tpl = (1,4,5,9,36,48)
n = int(input('Enter the element: '))
if n in tpl:
    print(tpl.index(n))
else:
    print('Not in tuple')