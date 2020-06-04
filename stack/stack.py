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
# from singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.__storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.__storage.append(value)

    def pop(self):
        if len(self.__storage) > 0:
            return self.__storage.pop()
        else:
            return None

    @property
    def size(self) -> int:
        return len(self.__storage)
