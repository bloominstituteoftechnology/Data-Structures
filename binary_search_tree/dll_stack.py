import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value): # add to head
        self.storage.add_to_head(value)
        self.size = self.storage.length

    def pop(self): #remove from head ? not 100% sure
        value  = None
        if self.size > 0:
            value = self.storage.remove_from_head()
            self.size = self.storage.length
        return value


    def len(self):
        self.size = self.storage.length
        return self.size
