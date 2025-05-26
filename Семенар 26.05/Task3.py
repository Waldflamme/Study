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

    def is_palindrome(self):
        left = self.head
        right = self.tail

        while left != None and right != None and left != right and left.prev != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True

dll = DoublyLinkedList()
for val in ["борщ", "суп", "салат", "суп", "борщ"]:
    dll.append(val)

print("Палиндром?" , dll.is_palindrome())