import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if data not in self.size:
      self.size.insert(0, item)
      return True
    return False
    pass
  
  def desize(self):
    if len(self.size) > 0:
      return self.size.pop()
  return ("size Empty!")
pass

  def len(self):
    return len(self.size)
    pass
