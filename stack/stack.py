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
        len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        self.storage.pop()

    def is_empty(self):
        self.storage == []

    def peek(self):
        if not self.is_empty():
            self.storage[-1]

    def get_stack(self):
        self.storage


s = Stack()

s.push('a')
s.push('b')
s.push('c')
print(s.storage)
s.pop()
s.pop()
print(s.storage)
