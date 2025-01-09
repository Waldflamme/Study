side1 = float(input('Enter first side length: '))
side2 = float(input('Enter second side length: '))
side3 = float(input('Enter third side length: '))
if side1<side2+side3 and side2<side1+side3 and side3<side1+side2:
    if side1**2==side2**2+side3**2 or side2**2==side3**2+side1**2 and side3**2==side1**2+side2**2:
        print ('Right triangle')
    else:
        print ('Non-right triangle')
else:
    print ('Can'"'"'t be a triangle')