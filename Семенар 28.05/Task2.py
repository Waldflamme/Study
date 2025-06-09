class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def sum_of_elements(head):
    if not head:
        return 0

    total = 0
    current = head

    while True:
        total += current.data
        current = current.next
        if current == head:
            break

    return total

n1 = Node(4)
n2 = Node(6)
n3 = Node(2)

n1.next = n2; n2.prev = n1
n2.next = n3; n3.prev = n2
n3.next = n1; n1.prev = n3

head = n1
print("Сумма элементов списка:", sum_of_elements(head))