class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def remove_greater_than(head, value):
    if not head:
        return None

    current = head
    start = head
    first_pass = True

    while True:
        next_node = current.next  # сохранить следующий узел

        if current.data > value:
            # Если список содержит только один элемент
            if current.next == current and current.prev == current:
                return None

            # Удаление текущего узла
            current.prev.next = current.next
            current.next.prev = current.prev

            # Обновление head, если удаляем голову
            if current == head:
                head = current.next

        current = next_node

        if current == start:
            if first_pass:
                first_pass = False
            else:
                break

    return head

def print_list(head):
    if not head:
        print("Список пуст.")
        return

    current = head
    while True:
        print(current.data, end=' ')
        current = current.next
        if current == head:
            break
    print()

n1 = Node(1)
n2 = Node(5)
n3 = Node(3)
n4 = Node(7)
n5 = Node(2)

n1.next = n2; n2.prev = n1
n2.next = n3; n3.prev = n2
n3.next = n4; n4.prev = n3
n4.next = n5; n5.prev = n4
n5.next = n1; n1.prev = n5

head = n1
print("До удаления:")
print_list(head)

head = remove_greater_than(head, 4)
print("После удаления (удаляем > 4):")
print_list(head)