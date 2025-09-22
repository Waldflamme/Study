import tkinter as tk
from tkinter import messagebox

'''Создаем функцию, вызываемую при нажатии кнопки'''
def convert_temperature():
    try:
        value = float(entry_input.get())  # читаем введённое число
        '''Проверка выбранного режима конвертации, соответствующие вычисления
           и вывод информации в поле результата'''
        if conversion_choice.get() == "CtoF": # Проверка выбора направления конвертации.
            # В нашем случае начинаем с проверки Цельсии в Фаренгейты.
            result = (value * 9/5) + 32 # Вычисление результата конвертации
            entry_output.delete(0, tk.END) # Очистка поля результата перед добавлением
            # очередного результата вычисления
            entry_output.insert(0, f"{result:.2f} °F") # Вставка результата в поле
            # результата с округлением до двух символов после запятой и вставкой значка фаренгейтов
        else:
            '''Аналогичные действия для конвертации фаренгейтов в цельсии'''
            result = (value - 32) * 5/9
            entry_output.delete(0, tk.END)
            entry_output.insert(0, f"{result:.2f} °C")
    except ValueError: # Вызов ошибки в случае ввода в поле ввода символов, отличных от цифр
        messagebox.showerror("Ошибка", "Введите число для конвертации")

# Главное окно
root = tk.Tk() # Создание главного окна приложения
root.title("Конвертер температур") # Установка окна заголовка
root.geometry("350x250") # Установка размеров окна в пикселях

# Ввод температуры
# Создание текстовой метки с пояснением для пользователя
label_input = tk.Label(root, text="Введите температуру:", font=("Arial", 12))
label_input.pack(pady=5) # Размещение элемента (текстовой метки) в окне с отступом 5
# пикселей по вертикали от верхней границы окна

'''Создание поля ввода исходной температуры с заданием цвета текста, фона и
   курсора (fg, bg, insertbackground соответственно'''
entry_input = tk.Entry(
    root, width=20, font=("Arial", 12),
    fg="black", bg="white", insertbackground="black"
)
entry_input.pack(pady=5) # Размещение поля ввода в окне с отступом 5 пикселей от
# предыдущего элемента

# Радиокнопки
'''Вставка пояснения для пользователя аналогично тому, как это было реализовано
   ранее в коде'''
label_mode = tk.Label(root, text="Выберите способ конвертации:", font=("Arial", 11))
label_mode.pack(pady=5)

'''Определение спец переменной StringVar, хранящей выбранное значение радиокнопок
   Устанавливаем CtoF (цельсии в фаренгейты) значением по умолчанию'''
conversion_choice = tk.StringVar(value="CtoF")

'''Создание радиокнопок для двух наших способов конвертации'''
radio_ctof = tk.Radiobutton(
    root, text="Из Цельсия в Фаренгейты", variable=conversion_choice, value="CtoF"
)
radio_ftoc = tk.Radiobutton(
    root, text="Из Фаренгейта в Цельсии", variable=conversion_choice, value="FtoC"
)

'''Добавление обоих радиокнопок в окно программы'''
radio_ctof.pack()
radio_ftoc.pack()

# Кнопка
'''Создание кнопки конвертации. Параметр command привязывает конкретную функцию к кнопке.
   Остальное выполняется по аналогии с предыдущими шагами'''
btn_convert = tk.Button(
    root, text="Конвертировать", command=convert_temperature, font=("Arial", 11)
)
btn_convert.pack(pady=10)

# Результат
'''Создание поля результата по аналогии с полем ввода'''
label_output = tk.Label(root, text="Результат:", font=("Arial", 12))
label_output.pack(pady=5)

entry_output = tk.Entry(
    root, width=20, font=("Arial", 12),
    fg="black", bg="white", insertbackground="black"
)
entry_output.pack(pady=5)

# Запуск приложения
root.mainloop()


