import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Not allowed to use lists

class Queue: # first in first out
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value): #
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        if self.is_empty():
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
