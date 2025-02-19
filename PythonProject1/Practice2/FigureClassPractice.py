import math

class Figure():
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def calculate(self, type_of_calculation):
        if type_of_calculation == 'area':
            return self.calculate_area()
        elif type_of_calculation == 'perimeter':
            return self.calculate_perimeter()
        else:
            return 'Неизвестный тип вычислений'



class Rectangle(Figure):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)




class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return math.pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def calculate_area(self):
        S = (self._side1+self._side2+self._side3)/2
        return (S*(S-self._side1)*(S-self._side2)*(S-self._side3))**0.5

    def calculate_perimeter(self):
        return self._side1+self._side2+self._side3



rectangle = Rectangle(10, 5)

rectangle_area = rectangle.calculate('area')
rectangle_perimeter = rectangle.calculate('perimeter')

circle = Circle(10)

circle_area = circle.calculate('area')
circle_perimeter = circle.calculate('perimeter')

triangle = Triangle(10,15,27)

triangle_area = triangle.calculate('area')
triangle_perimeter = triangle.calculate('perimeter')

print(f'Прямоугольник - площадь: {rectangle_area}, периметр: {rectangle_perimeter}')
print(f'Круг - площадь: {circle_area}, периметр: {circle_perimeter}')
print(f'Треугольник - площадь: {triangle_area}, периметр: {triangle_perimeter}')