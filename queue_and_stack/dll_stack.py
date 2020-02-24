import os
import sys

dll_path = os.path.normpath(os.path.join(__file__, "../../doubly_linked_list"))
sys.path.append(dll_path)

from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
            # adding and removing nodes has runtime O(1)

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
