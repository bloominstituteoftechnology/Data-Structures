class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        # appends new item to the end of the queue
        self.storage.append(item)
        self.size += 1

    def dequeue(self):
        # if size == 0, don't do anything, else pop first item from the storage
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        # length of self.storage
        self.size = len(self.storage)
        return self.size
