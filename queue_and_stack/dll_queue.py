import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


"""
https://he-s3.s3.amazonaws.com/media/uploads/cf1e1c1.png
Enqueue: Insert the element from the rear
Dequeue: Delete the element from the front 
"""

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
