side1 = float(input('Enter first side: '))
side2 = float(input('Enter second side: '))
side3 = float(input('Enter third side: '))
if side1<side2+side3 and side2<side1+side3 and side3<side1+side2:
    p = (side1 + side2 + side3)/2
    print('Area is: ', (p*(p - side1)*(p - side2)*(p - side3))**0.5)