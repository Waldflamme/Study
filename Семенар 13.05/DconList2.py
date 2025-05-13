class VisitorInfo:
    def __init__(self, first_name, last_name, visit_date, exhibits):
        self.first_name = first_name
        self.last_name = last_name
        self.visit_date = visit_date
        self.exhibits = exhibits

        self.prev = None
        self.next = None

    def __repr__(self):
        exhibits_str = ', '.join(f"{name} ({score}/5)" for name, score in self.exhibits.items())
        return f"{self.first_name} {self.last_name} | Дата: {self.visit_date} | Экспонаты: {exhibits_str}"

class MuseumVisitorList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, first_name, last_name, visit_date, exhibits):
        node = VisitorInfo(first_name, last_name, visit_date, exhibits)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def display_forward(self):
        print("Список посетителей (по времени входа):")
        current = self.head
        while current:
            print(current)
            current = current.next

    def display_backward(self):
        print("Список посетителей (в обратном порядке):")
        current = self.tail
        while current:
            print(current)
            current = current.prev

visitors = MuseumVisitorList()

visitors.append(
    "Анна", "Иванова", "2025-05-01",
    {"Мона Лиза": 5, "Звёздная ночь": 4}
)

visitors.append(
    "Петр", "Сидоров", "2025-05-02",
    {"Давид": 5, "Сотворение Адама": 5, "Тайная вечеря": 4}
)

visitors.append(
    "Елена", "Морозова", "2025-05-03",
    {"Крик": 3, "Герника": 4}
)

visitors.display_forward()
print()
visitors.display_backward()
