
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.insertion_point = 0
        self.buffer = []

    def append(self, item):
        self.buffer[self.insertion_point] = item
        if self.insertion_point < self.capacity:
            self.insertion_point = + 1
        else:
            self.insertion_point = 0

    def get(self):
        return self.buffer
