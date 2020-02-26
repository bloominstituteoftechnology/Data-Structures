import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    # Ans: DLL is a good choice to store elements of a stack since, 
    # are only accessed from the tail, in a stack, resulting to O(1) always
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_tail(value)
    self.size = self.storage.length

  def pop(self):
    value = False
    if self.size > 0:
      value = self.storage.remove_from_tail()
      self.size = self.storage.length
    return value

  def len(self):
    return self.size

    