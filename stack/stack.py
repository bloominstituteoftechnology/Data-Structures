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

from sys import path

path.append("../")
from singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.__storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.__storage.prepend(value)

    def pop(self):
        return self.__storage.remove_head()

    @property
    def size(self) -> int:
        return len(self.__storage)
