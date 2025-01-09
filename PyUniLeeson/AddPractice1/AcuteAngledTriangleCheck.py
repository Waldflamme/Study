side1 = float(input('Enter first side: '))
side2 = float(input('Enter second side: '))
side3 = float(input('Enter third side: '))
if side1**2<side2**2+side3**2 and side2**2<side1**2+side3**2 and side3**2<side1**2+side2**2 and side1<side2+side3 and side2<side1+side3 and side3<side1+side2:
    print('This is an acute-angled triangle')
else:
    print('This is not an acute-angled triangle or triangle at all')