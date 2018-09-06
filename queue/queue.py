
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    value = None 
    if(self.storage.head):
      value = self.storage.head.value
      self.storage.remove_head()
      self.size -= 1

    return value

  def len(self):
    return self.size

