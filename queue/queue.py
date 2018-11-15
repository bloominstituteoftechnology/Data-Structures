import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

#to add items to a queue yo ucan just use insert, to take items off use pop
class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if datavalue no in self.storage:
      self.storage.insert(0, datavalue)
        return True
      return False
  
  def dequeue(self):
    if len(self.size) > 0:
      return self.size.storage.pop()

  def len(self):
    return len(self.size)
