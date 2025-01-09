x = float(input('Enter x: '))
y = float(input('Enter y: '))
import math
a = math.exp(math.log((x+y)**3, 4))
b = (x*y)**0.5
print(round(a/b))