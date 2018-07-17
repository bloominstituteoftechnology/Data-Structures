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
# should add item to end of queue, so try add to tail here
 
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.remove_head()
    else:
      return None

# remove item from front of queue and return - this is like remove head
  def len(self):
    return self.size

# this seemed kind of self-explanatory to me
