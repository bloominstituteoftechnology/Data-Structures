import sys
sys.path.append('../linked_list')
from linked_list import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    if self.storage.head == None:
      return 0
    elif self.storage.head == self.storage.tail:
      return 1
    else:
      count = 1
      current_node = self.storage.head
      
      while current_node.next_node != None:
        count += 1
        current_node = current_node.next_node
      
      return count