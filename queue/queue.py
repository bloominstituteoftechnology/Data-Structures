import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

list = LinkedList()

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    list.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if not self.size:
        return None
      
    self.size -= 1
    
    return list.remove_head()

  def len(self):
    return self.size
