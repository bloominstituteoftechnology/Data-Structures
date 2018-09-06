import sys
from linked_list import LinkedList
sys.path.append('../linked_list')
class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      self.storage.remove_head
    return self.storage.remove_head()    

  def len(self):
    return self.size
