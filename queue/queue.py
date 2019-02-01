import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    #call linked_lists add to tail and it will add the item for us
    #then increment the size
    self.storage.add_to_tail(item)
    self.size += 1

  def dequeue(self):
    #first check if size is > than 0
    #if so then decrement by 1
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size
