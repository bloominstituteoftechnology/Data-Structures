import sys
import os

sys.path.append(f'{os.getcwd()}/linked_list')

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
    amount_of_nodes = 0
    current_node = self.storage.head
    while current_node is not None:
      amount_of_nodes += 1
      current_node = current_node.next_node
    return amount_of_nodes
