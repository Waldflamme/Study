from collections import deque

class UniqueQueue(object):
    def __init__(self):
        self.queue = deque()
        self.seen = set()

    def enqueue(self, item):
        if item not in self.seen:
            self.queue.append(item)
            self.seen.add(item)

    def __str__(self):
        return f'{list(self.queue)}'

q = UniqueQueue()
q.enqueue(5)
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)

print(q)
