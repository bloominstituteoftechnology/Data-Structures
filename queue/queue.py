import sys

sys.path.append('../linked_list')
from linked_list import LinkedList



class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  #add elements to queue
  def enqueue(self, item):
    #check to avoid dupe entry
    if item not in self.storage:
      self.storage.insert(0, item)
      return True
    return False

  #delete last item from queue
  def dequeue(self):
    if len(self.storage) > 0: 
      return self.storage.pop()
    return ("queue empty")

  def len(self):
    return len(self.storage)
