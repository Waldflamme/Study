import tkinter as tk
from tkinter import messagebox
import re
from abc import ABC, abstractmethod

# Создадим фабрику создания полей для ввода информации
'''Создаем фабрику для создания и валидации заполнения полей информации
   по контакту (фабричный метод)'''

class EntryFactory(ABC): # Создаем абстрактный базовый класс,
    # имеющий методы создания поля и его валидации

    @abstractmethod
    def create_entry(self, parent):
        """Создаёт виджет Entry внутри родительского контейнера."""
        pass

    @abstractmethod
    def validate(self, value):
        """Проверяет корректность введённого значения."""
        pass


'''Создаем классы конкретных продуктов (поля для информации) по контакту'''

# Рассмотрим конкретный продукт на примере поля имени
class NameEntryFactory(EntryFactory):
    def create_entry(self, parent): # Метод создания поля имени
        # Поле ввода для имени (ширина 50 символов)
        return tk.Entry(parent, width=50)

    def validate(self, value): # Метод валидации информации вводимой в поле имени
        # Имя: только буквы (латиница или кириллица) и пробелы
        if not value.strip(): # Проверка на наличие символов в строке
            return False, "Имя не может быть пустым."
        if not re.match(r"^[A-Za-zА-Яа-яЁё\s]+$", value): # Проверка, что используются
            # только разрешенные символы
            return False, "Имя должно содержать только буквы и пробелы."
        return True, ""
'''Далее идут аналогичные классы конкретных продуктов (полей телефона и e-mail) по аналогичному принципу'''

class PhoneEntryFactory(EntryFactory):
    def create_entry(self, parent):
        return tk.Entry(parent, width=30)

    def validate(self, value):
        # Телефон: 5–15 цифр, допускается + в начале
        if not re.match(r"^\+?\d{5,15}$", value):
            return False, "Телефон должен содержать 5–15 цифр (допустим знак + в начале)."
        return True, ""


class EmailEntryFactory(EntryFactory):
    def create_entry(self, parent):
        return tk.Entry(parent, width=50)

    def validate(self, value):
        # Простая проверка email для демонстрационных целей
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", value):
            return False, "Некорректный Email."
        return True, ""



# Функциональная часть приложения
'''Далее рассмотрим код, описывающий основной функционал приложения. Здесь будет 
   реализована фабрика полей, созданная выше, а также графический интерфейс приложения.'''

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление контактами")
        self.root.geometry("600x400")

        # Хранилище контактов: список кортежей (имя, телефон, email)
        self.contacts = []

        # Создание интерфейса
        self._create_widgets()

        # Фабрики для удобного доступа при валидации
        self.factories = {
            "name": NameEntryFactory(),
            "phone": PhoneEntryFactory(),
            "email": EmailEntryFactory()
        }

    # ---------- Создание всех виджетов ----------
    def _create_widgets(self):
        # ----- Поля ввода -----
        tk.Label(self.root, text="Имя:", font=("Arial", 11)).pack(pady=(10, 0))
        self.name_entry = NameEntryFactory().create_entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Телефон:", font=("Arial", 11)).pack(pady=(10, 0))
        self.phone_entry = PhoneEntryFactory().create_entry(self.root)
        self.phone_entry.pack()

        tk.Label(self.root, text="Email:", font=("Arial", 11)).pack(pady=(10, 0))
        self.email_entry = EmailEntryFactory().create_entry(self.root)
        self.email_entry.pack()

        # ----- Кнопки действий -----
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Добавить контакт",
                  command=self.add_contact).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Показать контакты",
                  command=self.show_contacts).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Очистить поля",
                  command=self.clear_fields).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Удалить выбранный",
                  command=self.delete_selected).grid(row=0, column=3, padx=5)

        # ----- Список контактов (Listbox) -----
        # Используем Listbox вместо Text для возможности выбора элемента
        tk.Label(self.root, text="Список контактов:", font=("Arial", 11)).pack()
        self.listbox_contacts = tk.Listbox(self.root, width=80, height=10)
        self.listbox_contacts.pack(pady=10)

    # ======================================================
    #                    ЛОГИКА ПРИЛОЖЕНИЯ
    # ======================================================

    def add_contact(self):
        """Добавить новый контакт после проверки данных."""
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        # --- Валидация полей через фабрики ---
        valid_name, msg = self.factories["name"].validate(name)
        if not valid_name:
            messagebox.showerror("Ошибка", msg)
            return

        valid_phone, msg = self.factories["phone"].validate(phone)
        if not valid_phone:
            messagebox.showerror("Ошибка", msg)
            return

        valid_email, msg = self.factories["email"].validate(email)
        if not valid_email:
            messagebox.showerror("Ошибка", msg)
            return

        # --- Добавление контакта в список ---
        self.contacts.append((name, phone, email))
        messagebox.showinfo("Успех", "Контакт добавлен!")
        self.clear_fields()

        # Автоматически обновим список в Listbox
        self.show_contacts()

    def show_contacts(self):
        """Отобразить все контакты в Listbox."""
        self.listbox_contacts.delete(0, tk.END)  # Очистить список
        if not self.contacts:
            self.listbox_contacts.insert(tk.END, "Список контактов пуст.")
        else:
            for idx, (name, phone, email) in enumerate(self.contacts, start=1):
                # Каждая строка содержит порядковый номер и данные
                self.listbox_contacts.insert(tk.END,
                    f"{idx}. {name} | {phone} | {email}"
                )

    def clear_fields(self):
        """Очистить все поля ввода."""
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def delete_selected(self):
        """
        Удалить выбранный в Listbox контакт.
        Если не выбран или список пуст — показать предупреждение.
        """
        selection = self.listbox_contacts.curselection()  # Индексы выбранных строк
        if not selection:
            messagebox.showwarning("Внимание", "Выберите контакт для удаления.")
            return

        index = selection[0]  # Берём первый выбранный элемент
        if not self.contacts:
            messagebox.showwarning("Внимание", "Список контактов пуст.")
            return

        # Удаляем контакт из хранилища
        # Важно: в Listbox нумерация начинается с 0,
        # а мы при показе контактов добавляли номер с 1, поэтому
        # индекс элемента соответствует индексу контакта в списке.
        del self.contacts[index]

        messagebox.showinfo("Удалено", "Контакт удалён.")
        self.show_contacts()  # Обновляем отображение



# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
