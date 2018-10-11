import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()
    
  def len(self):
    count = 0
    temp = self.storage.head
    while temp:
      count += 1
      temp = temp.next_node
    return count
