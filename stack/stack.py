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

'''
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
'''
class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.insert(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

'''
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
'''
import sys
sys.path.append('../singly_linked_list.py')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

'''
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   A: The methods you use to add and remove the elements are different. 
'''
