import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It is a very efficient structure to implement stacks. with a O(n) complexity.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        self.size -= 1
        value = self.storage.head.value
        self.storage.remove_from_head(value)
        return value

    def len(self):
        # return self.storage.__len__()
        return self.size


 