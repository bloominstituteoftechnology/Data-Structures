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

# Imports
from linkedList import Node
from linkedList import LinkedList

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.get_length()

    def push(self, value):
        self.storage.add_at_head(value)
        return

    def pop(self):
        return self.storage.remove_head()
