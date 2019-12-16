import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(None)

    def enqueue(self, value):
      self.size += 1
      self.storage.add_to_head(value)
      print(self.storage)

    def dequeue(self):
      if self.size > 0:
        self.size -= 1
        self.storage.remove_from_tail()
        print(self.storage)

    def len(self):
      return self.size

    def __str__(self):
      return f"the current queue is {self.storage}"
