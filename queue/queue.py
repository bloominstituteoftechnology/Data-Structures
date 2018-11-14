import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.insert(0, item)
  
  def dequeue(self):
    return self.storage.pop()

  def len(self):
    return len(self.storage)
