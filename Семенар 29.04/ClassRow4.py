from collections import deque

class CustomDeque:
    def __init__(self):
        self.queue = deque()

    def add_front(self, item):
        self.queue.appendleft(item)

    def add_back(self, item):
        self.queue.append(item)

    def remove_front(self):
        if self.queue:
            return self.queue.popleft()
        raise IndexError

    def remove_back(self):
        if self.queue:
            return self.queue.pop()
        raise IndexError

    def remove_min(self):
        if not self.queue:
            raise IndexError
        min_val = min(self.queue)
        self.queue.remove(min_val)
        return min_val

    def remove_max(self):
        if not self.queue:
            raise IndexError
        max_val = max(self.queue)
        self.queue.remove(max_val)
        return max_val

    def __str__(self):
        return f"{list(self.queue)}"

q = CustomDeque()

q.add_back(10)
q.add_front(5)
q.add_back(20)
q.add_front(1)

print(q)

q.remove_min()
print(q)

q.remove_max()
print(q)

q.remove_front()
print(q)

q.remove_back()
print(q)
