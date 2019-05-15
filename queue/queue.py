

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    storage_list = list()
    self.storage = storage_list

  def enqueue(self, item):
    self.storage.insert(0,item)
    self.size += 1
  
  def dequeue(self):
    if self.size == 0:
      return
    return self.storage.pop()

  def len(self):
    return self.size
