import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if item not in self.storage:
          self.storage.insert(0,item)
          return True
      return False
  
  def dequeue(self):
    if len(self.storage) > 0:
          return self.storage.pop()
      return ("No elements in Queue!")

  def len(self):
    return len(self.storage)
