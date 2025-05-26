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

    def find_first_index(self, target):
        if not self.head:
            return -1

        current = self.head
        index = 0

        while True:
            if current.value == target:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break

        return -1

cdll = CircularDoublyLinkedList()
for val in [7, 3, 5, 3, 9]:
    cdll.append(val)

print(cdll.find_first_index(3))
print(cdll.find_first_index(9))
print(cdll.find_first_index(100))