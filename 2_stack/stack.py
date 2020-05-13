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
   --> Array allow you to index to fetch particular elements
   --> LL ---> no index, they are like an anchor chain
made up of nodes that are connected to another
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size = len(self.storage)

    def pop(self):
        if self.size > 0:
            self.storage.pop()
            self.size = len(self.storage)
