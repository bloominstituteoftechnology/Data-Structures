import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack: # first in last out
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value): # in stacks, we add to the tail
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):          # and obviously, we always remove from the tail 
        if self.size > 0:
            self.size -=1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
