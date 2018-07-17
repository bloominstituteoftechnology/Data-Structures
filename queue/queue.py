# import sys
# sys.path.append('../linked_list')
# from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = list()

  def enqueue(self, item):
    if data not in self.size:
      self.size.insert(0, item)
      return True
    return False
    
  
  def dequeue(self):
    if self.size == 0:
      return None
      self.size -= 1
      sto = self.storage.remove()
      return sto
    

  def len(self):
    return self.size
    
