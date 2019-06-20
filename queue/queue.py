class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        # Answer: Linked List
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.pop()

    def len(self):
        return len(self.storage)
