side1 = float(input('Enter first side length: '))
side2 = float(input('Enter second side length: '))
side3 = float(input('Enter third side length: '))
if side1<side2+side3 and side2<side1+side3 and side3<side1+side2:
    if side1!=side2 and side1!=side3 and side2!=side3:
        print ('Scalene triangle')
    elif side1==side2 and side1==side3 and side1!=side3:
     print ('Isoscalane triangle')
    else:
        print ('Equilateral triangle')
else:
    print ('Can'"'"'t be a triangle')