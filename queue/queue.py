class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        return self

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0)

    def len(self):
        return len(self.storage)
