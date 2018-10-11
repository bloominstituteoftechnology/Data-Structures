import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if item == None:
      return None

    else:
       self.storage.add_to_tail(item)
       self.size += 1
  
  def dequeue(self):
    if self.size == 0:
      return None
    
    queue = self.storage.remove_head()
    self.size -= 1
    return queue

  def len(self):
    return self.size
    
