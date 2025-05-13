class List:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyConnectedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        list = List(data)
        if not self.head:
            self.head = self.tail = list
        else:
            list.prev = self.tail
            self.tail.next = list
            self.tail = list

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def print_list(self):
        print(','.join(map(str, self.to_list())))

def merge_sorted_doubly_connected_lists(list1, list2):
    merged = DoublyConnectedList()

    ptr1 = list1.head
    ptr2 = list2.head

    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            merged.append(ptr1.data)
            ptr1 = ptr1.next
        else:
            merged.append(ptr2.data)
            ptr2 = ptr2.next

    while ptr1:
        merged.append(ptr1.data)
        ptr1 = ptr1.next

    while ptr2:
        merged.append(ptr2.data)
        ptr2 = ptr2.next

    return merged

list1 = DoublyConnectedList()
for val in [4, 8, 12, 6, 15]:
    list1.append(val)

list2 = DoublyConnectedList()
for val in [13, 49, 19, 1, 99]:
    list2.append(val)

merged = merge_sorted_doubly_connected_lists(list1, list2)

list1.print_list()

list2.print_list()

merged.print_list()
