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

from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # Return the number of elements in a stack
        return self.size

    def push(self, value):
        # Increment the size by one
        self.size += 1
        # Add item to the top of the stack
        return self.storage.add_to_tail(value)

    def pop(self):
        # If array has at least one element:
        if self.size > 0:
            # Decrement the size
            self.size -= 1
            # Remove and return the element at the top of the stack
            return self.storage.remove_tail()
        return None
