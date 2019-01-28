import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # Put value [item] into the queue
    self.size += 1
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    # Take a vaue of of the queue from the front
    self.storage.remove_head()
    self.size -= 1
    

  def len(self):
    return self.size
    