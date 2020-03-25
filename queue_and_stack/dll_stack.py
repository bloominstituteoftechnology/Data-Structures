import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        #add element to the top of the stack
    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
        #remove element from the stack
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return



    def len(self):
        return self.size
