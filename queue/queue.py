import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
        self.storage.add_to_tail(item)
        return self.size
  
  def dequeue(self):
      if self.size > 0 and self.storage.remove_head is not None:
            self.size -= 1
            return self.storage.remove_head()

  def len(self):
    pass
