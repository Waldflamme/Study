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

    def sort_descending(self):
        if not self.head or self.head.next == self.head:
            return

        tail = self.head.prev
        tail.next = None
        self.head.prev = None

        self.head = self.insertion_sort_desc(self.head)

        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        current.next = self.head
        self.head.prev = current

    def insertion_sort_desc(self, head):
        if not head:
            return head

        sorted_head = None

        current = head
        while current:
            next_node = current.next
            current.prev = current.next = None
            sorted_head = self.sorted_insert_desc(sorted_head, current)
            current = next_node

        return sorted_head

    def sorted_insert_desc(self, head, node):
        if not head:
            return node

        current = head
        while current and current.value > node.value:
            current = current.next

        if not current:
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = node
            node.prev = tail
        elif current == head:
            node.next = head
            head.prev = node
            head = node
        else:
            prev_node = current.prev
            prev_node.next = node
            node.prev = prev_node
            node.next = current
            current.prev = node

        return head

cdll = CircularDoublyLinkedList()
for val in [5, 3, 7, 3, 9, 5, 1]:
    cdll.append(val)

print("До сортировки:")
cdll.print_list()

cdll.sort_descending()

print("После сортировки по убыванию:")
cdll.print_list()