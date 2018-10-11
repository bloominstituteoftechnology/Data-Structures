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
    length = 0
    curr_node = self.storage.head
    if curr_node:
      while (curr_node.next_node):
        length += 1
        curr_node = curr_node.next_node
      if curr_node.next_node is None:
        length += 1
    return length