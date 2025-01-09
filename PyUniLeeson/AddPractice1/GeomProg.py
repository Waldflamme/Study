a,b,c,d = map(int, input('Enter four nums: ').split())
if b == (a*c)**0.5 and c == (b*d)**0.5:
    print('This is geometrical progression')
else:
    print('This is not geometrical progression')