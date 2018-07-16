import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    if item not in self.queue:
      self.queue.insert(0, item)
      return True
    return False

  def dequeue(self):
    if len(self.queue)>0:
      return self.queue.pop()
    return False

  def len(self):
    return len(self.queue)
