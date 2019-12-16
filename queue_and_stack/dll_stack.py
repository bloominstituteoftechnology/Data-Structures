import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because it has all of the methods we need to create and manipulate a stack, without having to rewrite code
        self.storage = DoublyLinkedList(None)

    def push(self, value):
      self.size += 1
      return self.storage.add_to_head(value)

    def pop(self):
      if self.size > 0:
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
      return self.size

    def __str__(self):
      return f"Stack is {self.storage}"