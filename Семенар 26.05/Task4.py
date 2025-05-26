class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def split_by_value(self, threshold):
        less_list = DoublyLinkedList()
        greater_equal_list = DoublyLinkedList()

        current = self.head
        while current:
            if current.value < threshold:
                less_list.append(current.value)
            else:
                greater_equal_list.append(current.value)
            current = current.next

        return less_list, greater_equal_list

dll = DoublyLinkedList()
for val in [10, 5, 18, 3, 12, 7, 25]:
    dll.append(val)

print("Исходный список:")
dll.print_list()

less, greater_equal = dll.split_by_value(10)

print("\nМеньше 10:")
less.print_list()

print("\nБольше или равно 10:")
greater_equal.print_list()