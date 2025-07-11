#Задать два двухмерных массива ar1 и ar2 размерности (10, 4), состоящих из случайных целых чисел в пределах от -5 до 5.
#Удвоить все значения ar1, которые больше значений ar2, расположенных на аналогичных позициях, остальные значения сделать равными 0.
#Решить задачу средствами numpy и/или pandas. Не использовать циклы и конструкции стандартного Python там, где можно использовать возможности данных библиотек.

import numpy as np

# Шаг 1: создание массивов размерности (10, 4) со случайными целыми значениями от -5 до 5 включительно
ar1 = np.random.randint(-5, 6, size=(10, 4))
ar2 = np.random.randint(-5, 6, size=(10, 4))

# Шаг 2: сравнение элементов: ar1 > ar2 вернёт булевый массив той же размерности
# где True — значит, элемент в ar1 больше, чем в ar2
mask = ar1 > ar2

# Шаг 3: применение маски: где True — удваиваем элемент ar1, где False — ставим 0
result = np.where(mask, ar1 * 2, 0)

# Шаг 4: выводим результат
print("ar1:\n", ar1)
print("ar2:\n", ar2)
print("Результат:\n", result)