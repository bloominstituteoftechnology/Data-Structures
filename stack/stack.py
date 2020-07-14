"""
~ Stack is a Data Structure ~

1. Implement the Stack class using an array as the underlying storage structure.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
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
        self.storage.append(value)

    def pop(self):
        if len(self)>0:
            return self.storage.pop()
        else:
            return None
