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
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    # length = 0
    # h = self.storage.head
    # while h:
    #   length += 1
    #   h = h.get_next()
    # return length
    return self.size
