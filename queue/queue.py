import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # Put value [item] into the queue
    size += 1
    pass
  
  def dequeue(self):
    # Take a vaue of of the queue from the front
    size -= 1
    pass

  def len(self):
    return self.size
    pass
