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
from linked_list import Node, LinkedList

class Stack:
    def __init__(self, ls=[]):
        self.size = 0
        self.storage = ls

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop(-1)


