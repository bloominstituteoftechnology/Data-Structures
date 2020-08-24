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

# Stack using an array
# class Stack:
#     def __init__(self):
#         self.items = []

#     def __len__(self):
#         return len(self.items)

#     def push(self, value):
#         self.items.insert(0, value)

#     def pop(self):
#         if self.items != []:
#             return self.items.pop(0)
#         else:
#             return None

# Stack using a Linked List
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.items = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.items.add_to_head(value)
        

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.items.remove_head()
            
