import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

# Main idea: import the LinkedList data structure and build another one

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size

# Alternative:

# class Queue:
#   def __init__(self):
#     self.storage = []

#   def enqueue(self, item):
#     self.storage.append(item)
  
#   def dequeue(self):
#     if len(self.storage) > 0:
#       return self.storage.pop(0)
#     return None

#   def len(self):
#     return len(self.storage)