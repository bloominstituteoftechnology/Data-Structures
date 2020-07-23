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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)
        return

    def pop(self):
        # Is our underlying list empty?
        if len(self.storage) == 0:
            return None

        # Grab the return value
        tmp_val = self.storage[0]
        
        if len(self.storage) == 1:
            self.storage = []

        if len(self.storage) > 1:
            self.storage = self.storage[1:]

        return tmp_val
