import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def push(self, value):
    return self.storage.push(value)
  
  def pop(self):
    if len(self.storage) < 1:
      return None
    return self.storage.pop()

  def len(self):
    return len(self.storage)
