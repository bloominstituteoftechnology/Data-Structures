"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
            
        self.size -= 1
        popped_value = self.storage.remove_from_tail()

        return popped_value