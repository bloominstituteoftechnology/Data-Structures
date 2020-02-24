import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # pass
        self.storage.add_to_tail(value)
        self.size += 1        

    def pop(self):
        # pass
        value = self.storage.remove_from_tail()
        if not value==None:
            self.size -= 1
        return value

    def len(self):
        return self.size
