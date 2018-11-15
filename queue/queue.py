import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
      self.size = 0
      self.storage = LinkedList()

  def enqueue(self, item):
      if self.size > 0:
          self.item.enqueue(item)

  def dequeue(self):
      if self.size > 0:
          self.size.dequeue(-1)

  def len(self):
      # TO DO
