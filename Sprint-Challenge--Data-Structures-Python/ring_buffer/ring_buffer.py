class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 1

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.insert(self.count-1, item)
            self.storage.pop(self.count)
            self.count += 1
            if self.count > self.capacity:
                self.count = 1
        elif len(self.storage) < self.capacity:
            self.storage.insert(len(self.storage), item)

    def get(self):
        return self.storage
