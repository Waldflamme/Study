ln = input('Enter a line: ')
tpl = tuple(ln)
print(tpl)
if tpl[::]==tpl[::-1]:
    print('It'"'"'s symmetric')
else:
    print('It'"'"'s not symmetric')