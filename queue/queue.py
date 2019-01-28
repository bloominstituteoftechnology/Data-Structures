import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    # to get the length check first check if there is a length
    # get the value of the current head
    current_head = self.storage.head
    # check if current head exist
    if current_head == None:
      return 0
    if current_head.get_next() == None:
      return 1
    else:
      count = 1
      while current_head.get_next() is not None:
        count += 1
        current_head = current_head.get_next()
      return count

