import sys
sys.path.append('../linked_list')

class Queue:
  def __init__(self):
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    
  
  def dequeue(self):
    if len(self.storage) > 0:
      return self.storage.pop(0)
    return None

  def len(self):
    return len(self.storage)
