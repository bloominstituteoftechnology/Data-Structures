import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #it is a good choice because it allows us to use our created functions to get these 
        #stack and queue methods to work more efficiently 
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0: 
            return None
        else: 
            popped_head = self.storage.remove_from_head()
            self.size -=1 
        return popped_head

    def len(self):
        return self.size
