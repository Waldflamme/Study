from collections import deque

class LimitedQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError
        self.queue = deque(maxlen=capacity)
        self.capacity = capacity

    def enqueue(self, item):
        self.queue.append(item)

    def __str__(self):
        return f"{list(self.queue)}"

q = LimitedQueue(3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)

q.enqueue(40)
print(q)