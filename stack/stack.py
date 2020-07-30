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
sys.path.append('singly_linked_list')
from singly_linked_list import LinkedList # pylint: disable=import-error

# 1. Stack (using an array)
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     # len performance: O(1)
#     def __len__(self):
#         return self.size

#     # push performance: O(1)
#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     # pop performance: O(1)
#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()


# 2. Stack (using a linked list)
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def isEmpty(self):
        return self.size == 0

    # len performance: O(1)
    def __len__(self):
        return self.size

    # push performance: O(1)
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    # pop performance: O(1)
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

# 3. In terms of the implementation, both Stacks are nearly identical with only the 
# method names differing. In terms of performance, the push and pop methods for both
# implementations are O(1). Note that the LinkedList's remove_tail method has a 
# performance of O(n). So in order for the LinkedList implementation to acheive a
# performance of O(1), the Stack must be implemented so that 'head' of the LinkedList 
# represents the 'top' of the Stack. This is different from the array implementation
# where last index in the array represents the 'top' of the Stack.