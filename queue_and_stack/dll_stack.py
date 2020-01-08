import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

#LIFO

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else: 
            return None

    def len(self):
        return self.size
