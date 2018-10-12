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
    if self.size > 0:
      self.size -= 1
    return self.storage.remove_head()

  def len(self):
    return self.size

# LAST IN FIRST OUT
# FIRST IN FIRST OUT
# QUEUE IS A LIST OR COLLECTION WITH THE RESTRICTION THAT INSERTION CAN BE PERFORMED AT ONE END (BACK) AND DELETION CAN BE PERFORMED AT OTHER END (FRONT)
