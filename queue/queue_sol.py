import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    # counter to keep track of the number of elements in our queue
    self.size = 0
    # we'll use our LinkedList implementation to build the queue
    self.storage = LinkedList()

  def enqueue(self, item):
    # add the item to the linked list 
    self.storage.add_to_tail(item)
    # increment our size counter
    self.size += 1
  
  def dequeue(self):
    # decrement our size counter
    self.size -= 1
    # remove the head of the linked list and return it
    return self.storage.remove_head()

  def len(self):
    return self.size