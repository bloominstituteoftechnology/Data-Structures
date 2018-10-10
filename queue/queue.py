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
    counter = 0
    node = self.storage.head
    while node:
      counter += 1
      node = node.next_node
    self.size = counter
    return self.size
