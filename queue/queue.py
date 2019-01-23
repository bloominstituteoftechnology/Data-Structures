import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    pass
  
  def dequeue(self):
    return self.storage.remove_head()
    pass

  def len(self):
    if self.storage.head is None:
      return 0
    node = self.storage.head
    count = 1
    while node.get_next() is not None:
      node = node.get_next()
      count += 1
    return count
    pass
