import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    # add the item to the tail of the storage of the queue
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    # TODO: add some logic here
    self.storage.remove_head()

  def len(self):
    # TODO: do some length / size setting in this method with some logic after a coffee break
    return self.size
