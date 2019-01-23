import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    self.storage.remove_head()

  def len(self):
    current_node = self.storage.head
    while current_node:
      self.size += 1
      current_node = current_node.get_next()

    return self.size
