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

    def __str__(self):
        if self.size == 0:
            return 'the Stack is empty'
        n = 0
        output = ''
        while n < self.size:
            output += f'\n[{self.storage[n]}]'
            n += 1
        return output

    def __len__(self):
        if self.size == 0:
            return 0
        else:
            return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        value = self.storage[-1]
        self.storage.pop()
        self.size -= 1
        return value