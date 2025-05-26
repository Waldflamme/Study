class OrderList:
    def __init__(self, dish_name, price, quantity, order_date, status):
        self.dish_name = dish_name
        self.price = price
        self.quantity = quantity
        self.order_date = order_date
        self.status = status

        self.prev = None
        self.next = None

class OrderLs:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, dish_name, price, quantity, order_date, status):
        new_node = OrderList(dish_name, price, quantity, order_date, status)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_orders(self):
        current = self.head
        while current:
            print(f"Блюдо: {current.dish_name}, Цена: {current.price}, Кол-во: {current.quantity}, "
                  f"Дата: {current.order_date}, Статус: {current.status}")
            current = current.next

orders = OrderLs()
orders.add_order("Борщ", 250, 2, "2025-05-25", "в обработке")
orders.add_order("Пицца", 500, 1, "2025-05-25", "готов")
orders.add_order("Суши", 650, 3, "2025-05-25", "доставлен")

orders.display_orders()