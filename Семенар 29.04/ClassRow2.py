from collections import deque

class FilteredQueue:
    def __init__(self, even_only=True):
        self.queue = deque()
        self.even_only = even_only

    def enqueue(self, item):
        if isinstance(item, int):
            if self.even_only and item % 2 == 0:
                self.queue.append(item)
            elif not self.even_only and item % 2 != 0:
                self.queue.append(item)

    def __str__(self):
        return f"{list(self.queue)}"

even_queue = FilteredQueue(even_only=True)
even_queue.enqueue(2)
even_queue.enqueue(3)
even_queue.enqueue(4)
print(even_queue)

odd_queue = FilteredQueue(even_only=False)
odd_queue.enqueue(1)
odd_queue.enqueue(6)
odd_queue.enqueue(9)
print(odd_queue)