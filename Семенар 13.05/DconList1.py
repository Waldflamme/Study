class PurchaseNode:
    def __init__(self, name, price, quantity, date):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.date = date

        self.prev = None
        self.next = None

    def __repr__(self):
        return f"{self.name} | {self.price}₽ | {self.quantity} шт. | {self.date}"

class PurchaseDoublyConnectedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, name, price, quantity, date):
        node = PurchaseNode(name, price, quantity, date)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def display_forward(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(current)
            current = current.prev

purchases = PurchaseDoublyConnectedList()

purchases.append("Сыр", 150, 1, "2025-05-01")
purchases.append("Колбаса", 300, 2, "2025-05-03")
purchases.append("Масло", 200, 1, "2025-05-05")

print("Покупки в прямом порядке:")
purchases.display_forward()

print("\nПокупки в обратном порядке:")
purchases.display_backward()