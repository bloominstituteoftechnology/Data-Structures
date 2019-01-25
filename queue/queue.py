import sys
sys.path.extend('../linked_list')
from linked_list.linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if self.storage.head is None:
      self.size = 0
      return None
    else:
      self.size -= 1
      return self.storage.remove_head()

  def len(self):
    return self.size

