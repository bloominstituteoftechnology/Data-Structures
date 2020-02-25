import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


"""
https://he-s3.s3.amazonaws.com/media/uploads/defd4ad.png
Push: Andd/Insert element to the head
Pop: Delete element from the head
"""
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because DLL use a dynamic allocation of data whereas in the array
        # using pointers that aloows to track the elements
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
    def len(self):
        return self.size
