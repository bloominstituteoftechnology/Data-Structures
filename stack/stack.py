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

sys.path.append('../singly_linked_list/')
from singly_linked_list import LinkedList


# class Stack:
#     def __init__(self):
#         # Each time an item from the stack gets removed or added, decrement/increment the self.size
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         # Return length of self.storage
#         return len(self.storage)
#
#     def push(self, value):
#         # Increment self.size
#         self.size += 1
#         # Adds the incoming value to the top of the stack / storage list
#         return self.storage.append(value)
#
#     def pop(self):
#         # Check if storage is not empty
#         if len(self.storage) != 0:
#             # Decrement self.size
#             self.size -= 1
#             # Removes last item of self.storage
#             return self.storage.pop()
#
#

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # Return the length of the SLL
        return self.size

    def push(self, value):
        self.size += 1
        # Invoke add_to_tail
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            # Invoke remove_tail
            return self.storage.remove_tail()


# Creates a new stack
s1 = Stack()

# Successfully prints the size
print(f'Size: {s1.__len__()}')
# Successfully adds item
s1.push(1)
# Successfully prints the size when incremented
print(f'Size: {s1.__len__()}')
s1.push(2)
s1.push(3)
print(s1.storage)
# Successfully removes item
s1.pop()
print(s1.storage)
# Successfully prints the size when decremented
print(f'Size: {s1.__len__()}')
