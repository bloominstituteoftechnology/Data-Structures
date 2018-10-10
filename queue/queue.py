import sys
sys.path.append('../linked_list')
from linked_list import LinkedList 


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size = self.size + 1
  
  def dequeue(self):
    self.storage.remove_head()
    if self.size > 0:
      self.size = self.size - 1
    else: 
      self.size = 0
      
  def len(self):
    return self.size
