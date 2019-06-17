class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)
        self.size += 1

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()

    def len(self):
        return len(self.storage)
