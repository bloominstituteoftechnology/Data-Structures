import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if item == None:
      return 0
    elif self.storage.get_length == 0:
      return 0
    self.storage.add_to_tail(item)
    
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    count = 0
    counter = self.storage.head
    while counter:
      count += 1
      counter = counter.get_next()
    return count    
