class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            tail = self.head.prev

            tail.next = new_node
            new_node.prev = tail

            new_node.next = self.head
            self.head.prev = new_node

    def remove_node(self, node):
        if node.next == node:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.head == node:
                self.head = node.next

    def remove_duplicates(self):
        if not self.head or self.head.next == self.head:
            return

        seen = set()
        current = self.head

        while True:
            if current.value in seen:
                node_to_remove = current
                current = current.next
                self.remove_node(node_to_remove)
            else:
                seen.add(current.value)
                current = current.next

            if current == self.head:
                break

    def print_list(self):
        if not self.head:
            print("Список пуст")
            return

        current = self.head
        result = []
        while True:
            result.append(str(current.value))
            current = current.next
            if current == self.head:
                break
        print(" <-> ".join(result))

cdll = CircularDoublyLinkedList()
for val in [5, 3, 7, 3, 9, 5, 1]:
    cdll.append(val)

print("До удаления дублей:")
cdll.print_list()

cdll.remove_duplicates()

print("После удаления дублей:")
cdll.print_list()