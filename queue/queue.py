class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    pass
    # self.storage[:0] = item?
  
  def dequeue(self):
    # self.storage.pop()?

  def len(self):
   return len(self.storage)
