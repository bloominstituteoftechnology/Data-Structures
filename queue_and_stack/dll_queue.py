import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because it has all of the methods we need to create and manipulate a Queue, without having to rewrite code
        self.storage = DoublyLinkedList(None)

    def enqueue(self, value):
      self.size += 1
      return self.storage.add_to_head(value)

    def dequeue(self):
      if self.size > 0:
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
      return self.size

    def __str__(self):
      return f"Queue is {self.storage}"
