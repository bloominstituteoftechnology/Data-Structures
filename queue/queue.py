import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1
  
  def dequeue(self):
    val = self.storage.remove_head()
    if val:
      self.size -= 1
    return val
    
  def len(self):
    return self.size

queue = Queue()

print(queue.storage)