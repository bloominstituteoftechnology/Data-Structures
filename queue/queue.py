import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    # initializes size of queue
    self.size = 0
    # initializes items in storage
    self.storage = LinkedList()

  def enqueue(self, item):
    # when adding new item to storage it adds one to size
    # we add 1 first because add_to_tail() will break us out of this function when it returns
    self.size += 1
    # adds another value to the tail of storage
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    # sets remove_value to the value of remove_head()
    remove_value = self.storage.remove_head()
    if remove_value == None:
      # if there is no value to remove then return None
      return None
    # if there is a value and it is removed subtract 1 from size
    self.size -= 1
    # return the value of removed item
    return remove_value

  def len(self):
    # returns the value of size
    return self.size
