from collections import deque

class FilteredQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def remove_bigger(self, value):
        self.queue = deque(x for x in self.queue if x <= value)

    def __str__(self):
        return f"{list(self.queue)}"

q = FilteredQueue()

q.enqueue(10)
q.enqueue(5)
q.enqueue(20)
q.enqueue(7)
q.enqueue(3)

print(q)

q.remove_bigger(7)
print(q)