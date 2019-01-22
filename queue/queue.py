import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

#adding items
  def enqueue(self, item):
   self.storage.add_to_tail(item)
   self.size += 1

#deleting items 
  def dequeue(self):
    # is a node in storage?
    if self.storage.head == None:
     return None

    else:
      prev_head = self.storage.head.value
      self.storage.remove_head()
      return prev_head

#size of 
  def len(self):
    current_head = self.storage.head
    if current_head == None:
      self.size = 0
      return self.size
    
    if current_head.get_next() == None:
      self.size = 1
      return self.size

    else:
      count = 1
      while current_head.get_next() != None:
        count += 1
        current_head = current_head.get_next()
        self.size = count
      return self.size

    return self.size


