# singly_linked_list/stack.py

from singly_linked_list import LinkedList, Node

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

   Subjectively, the key differnce is that the latter is more difficult.
   Python lists (arrays) were specifically designed to be able to implement
   stacks, see https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-stacks.
"""
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
        else:
            result = self.storage.remove_tail()
            self.size -= 1
            return result
