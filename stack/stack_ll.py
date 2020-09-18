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

# https://www.geeksforgeeks.org/stack-in-python/
"""

from singly_linked_list import LinkedList

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.remove_tail()

"""
Ran 4 tests in 0.000s

OK
"""