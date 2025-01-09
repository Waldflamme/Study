num1 = str(input('Enter first complex number: '))
num2 = str(input('Enter second complex number: '))
print('Real parts sum',complex(num1).real+complex(num2).real)
print('Imaginary part substraction',complex(num1).imag-complex(num2).imag)
#(var).real - вещественная часть комплексного числа
#(var).imag - мнимаая часть комплексного числа
#complex(var) - может преобразовывать тип данных "строка" в комплексное число