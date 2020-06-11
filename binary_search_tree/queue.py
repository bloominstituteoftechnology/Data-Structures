class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)        

    def enqueue(self, value):
        self.storage.append(value)
        # self.size += 1
          

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            # self.size -= 1
            return self.storage.pop(0)