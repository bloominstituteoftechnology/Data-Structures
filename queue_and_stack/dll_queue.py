import os
import sys

dll_path = os.path.normpath(os.path.join(__file__, "../../doubly_linked_list"))
sys.path.append(dll_path)

from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
            # adding and removing nodes has runtime O(1)
        

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return len(self.storage)
