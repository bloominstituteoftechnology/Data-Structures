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
from linked_list import Node, LinkedList
# Arrays
# class Stack:
#     def __init__(self, ls=[]):
#         self.size = 0
#         self.storage = ls

#     def __len__(self):
#         if self.size <= 0:
#             return 0
#         else:
#             return self.size

#     def push(self, value):
#         self.size +=1
#         return self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size += -1
#             return self.storage.pop(-1)


# Linked Lists
class Stack:
    def __init__(self):
        self.size = 0
        self.link = LinkedList()
        self.top = None

    def __len__(self):
        if self.size <= 0:
            return 0
        else:
            return self.size

    def push(self, value):
        self.size +=1
        self.link.add_to_tail(value)
        self.top = self.link.tail

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.top = self.link.remove_tail()
            self.size += -1
            return self.top

