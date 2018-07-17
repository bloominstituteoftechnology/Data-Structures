import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
      self.size = 0
      self.storage = LinkedList()

  def enqueue(self, item):
      self.storage.add_to_tail(item)
      self.size += 1
  
  def dequeue(self):
      if self.storage.head is None: return None
      head = self.storage.head
      self.storage.remove_head()
      self.size -= 1
      return head.get_value()

  def len(self):
      return self.size
