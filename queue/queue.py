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
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList, Node

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1
#         return None

#     def dequeue(self):
#         if self.size != 0:
#             item = self.storage[0]
#             del self.storage[0]
#             self.size -= 1
#             return item
#         else:
#             return None

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size = self.size + 1
        self.storage.add_to_tail(value)
        return None

    def dequeue(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_head()
        else:
            return None

