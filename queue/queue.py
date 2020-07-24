"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

import sys
sys.path.extend(['singly_linked_list', 'stack'])
from singly_linked_list import LinkedList # pylint: disable=import-error
from stack import Stack # pylint: disable=import-error

# 1. Queue (using an array)
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     # len performance: O(1)
#     def __len__(self):
#         return self.size

#     # enqueue performance: O(1)
#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     # dequeue performance: O(n)
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)


# 2. Queue (using a linked list)
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     # len performance: O(1)
#     def __len__(self):
#         return self.size

#     # enqueue performance: O(1)
#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     # dequeue performance: O(1)
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_head()


# 3. In terms of the implementation, both Queues are nearly identical with only the 
# method names differing. In terms of performance, however, the array implementation
# takes O(n) to dequeue an element, compared to O(1) for the linked list implementation.


# Stretch: Queue (using a stack)
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
        self.temp_storage = Stack()
    
    # len performance: O(1)
    def __len__(self):
        return self.size

    # enqueue performance: O(1)
    def enqueue(self, value):
        self.storage.push(value)
        self.size += 1

    # dequeue performance: O(n)
    def dequeue(self):
        if self.size == 0:
            return None

        self.size -= 1

        while len(self.storage) > 1:
            self.temp_storage.push(self.storage.pop())
        elem_popped = self.storage.pop()

        while len(self.temp_storage) > 0:
            self.storage.push(self.temp_storage.pop())
        
        return elem_popped