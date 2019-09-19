from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()
  
  def __str__(self):
    return f"{self.storage}"

  def push(self, value):
    added = self.storage.add_to_tail(value)
    self.size += 1
    return added
  
  def pop(self):
    if self.size > 0:
      self.size -= 1
      removed = self.storage.remove_from_tail()
      return removed
    else:
      return None


  def len(self):
    return self.size
