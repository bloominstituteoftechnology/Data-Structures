class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)
        self.size = len(self.storage)

    def dequeue(self):
        if self.size == 0:
            return None
        popped_item = self.storage.pop()
        self.size = len(self.storage)
        return popped_item

    def len(self):
        return self.size
