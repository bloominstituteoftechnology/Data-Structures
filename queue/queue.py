import sys
import queue
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.item = []

  def enqueue(self, item):
    self.item.insert(0, item)
  
  def dequeue(self):
    queue = self.item
      if queue == 0:
        print("Theres nothing there")
      else:
        return self.item.pop()

  def len(self):
    return len(self.item)
