class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)

    def dequeue(self):
        if len(self.storage) == 0:
            pass
        else:
            removed_item = self.storage.pop()
            return removed_item

    def len(self):
        return len(self.storage)
