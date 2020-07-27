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
sys.path.append('C:/Users/Rob/repos/Data-Structures/')
from singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self): 
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_tail(value)
        # self.storage.length += 1

    def pop(self):
        if self.storage.length > 0:
            return self.storage.remove_tail()
            # self.storage.length -= 1
        else:
            return None