import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue: # first in first out
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value): # we add to head
    # check the base case
        self.size += 1
        self.storage.add_to_head(value)


    def dequeue(self):

        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):

        return self.size
