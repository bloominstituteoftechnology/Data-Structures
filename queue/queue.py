class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1
  
  def dequeue(self):
    head = self.storage[0]
    self.storage = self.storage[0:]
    self.size -= 1

  def len(self):
    return self.size
