from linked_list import LinkedList
from linked_list import Node
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
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
    #    self.storage.unshift(value)
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) != 0:
            del self.storage[0]

stack = Stack()
stack.push(9)
stack.push(10)
stack.push(105)
for i in stack.storage:
    print(i)
stack.pop()
for i in stack.storage:
    print(i)
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) != 0:
            return self.storage.pop(0)


stack = Stack()
stack.push(9)
stack.push(10)
stack.push(105)
for i in stack.storage:
    print(i)
stack.pop()
for i in stack.storage:
    print(i)