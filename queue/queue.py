class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    return self.storage.insert(0, item)
  
  def dequeue(self):
    if len(self.storage):
      return self.storage.pop()

  def len(self):
    return len(self.storage)


