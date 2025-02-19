import numpy as np

print("Задание 1")
print()
# Считываем данные из файла, пропуская первую строку (заголовки)
data = np.loadtxt('minutes_n_ingredients.csv', delimiter=',', dtype=np.int32, skiprows=1)

# Выводим первые 5 строк массива
print("Первые 5 строк массива:")
print(data[:5])

print()
print("Задание 2")
print()
# Извлечение второго и третьего столбцов (все столбцы, кроме первого)
columns = data[:, 1:]

# Вычисление статистик для каждого столбца
mean_values = np.mean(columns, axis=0)  # Среднее значение
min_values = np.min(columns, axis=0)    # Минимум
max_values = np.max(columns, axis=0)    # Максимум
median_values = np.median(columns, axis=0)  # Медиана

# Вывод результатов
print("Средние значения:", mean_values)
print("Минимумы:", min_values)
print("Максимумы:", max_values)
print("Медианы:", median_values)

print()
print('Задание 3')
print()

second_column = data[:,1]
q_75 = np.quantile(second_column, 0.75)
data2 = data.copy()
data2[:,1] = np.minimum(data2[:,1], q_75)
print(q_75)
print(data2)

print()
print('Задание 4')
print()

data3 = data.copy()
data3[second_column == 0,1] = 1

print('Пример на 693 строке')
print(data[691])
print(data3[691])

print()
print('Задание 5')
print()

uniq = np.unique(data[:,0])
print(len(uniq))

print()
print('Task 6')
print()

uniq1 = np.unique(data[:,3])
print(len(uniq1),uniq1)

print()
print('Task 7')
print()



