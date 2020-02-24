import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# Not allowed to use lists

class Stack:# In a stack, a new element is added at one end and an element is removed from that end only. 
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
