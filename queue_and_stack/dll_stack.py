import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        pass

    def len(self):
        pass
