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

sys.path.append("../singly_linked_list")
from singly_linked_list import LinkedList, Node


# The code that was wrong with the test
# Specifics: Couldn't pass the self.assertIsNone(self.stack.pop()) on line 40
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#         # self.storage = ?
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.size += 1
#         self.stack.append(value)
#
#     def pop(self):
#         self.size -= 1
#         # if not IndexError:
#         return self.stack.pop()
#         # else:
#         #     return None

# Array version of stack
class Stack:
    def __init__(self):
        self.storage = []
        # self.storage = ?

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()


# Linked List Implementation
# class Stack(LinkedList):
#     def __init__(self):
#         super().__init__()
#         self.size = 0
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.add_to_head(value)
#         self.size += 1
#
#     def pop(self):
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.remove_head()
