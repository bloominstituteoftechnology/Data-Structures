from collections import deque


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = deque()

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            self.size -= 1
            return self.storage.popleft()
        return None

    def len(self):
        return self.size

    def is_empty(self):
        return self.len() == 0
