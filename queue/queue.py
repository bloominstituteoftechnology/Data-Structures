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
  
  def dequeue(self):
    self.size -= 1
    self.storage.remove_head()

  def len(self):
    return self.size
