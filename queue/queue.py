class Queue_Array:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
