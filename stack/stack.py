"""
1. Implement the Stack class using an array as the underlying storage structure.
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self)>0:
#             return self.storage.pop()
#         else:
#             return None

"""
    Re-implement the Stack class, 
    using the linked list implementation as the underlying storage structure.
"""
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1 
        self.storage.add_to_tail(value)
    
    def pop(self):
        if self.size == 0:
            return None
        else: # Remove off bottom LIFO
            self.size -= 1 
            return self.storage.remove_tail()

        
"""
    Difference between using an array vs. linked list for a Stack?
        Arrays have runtime complexity of O(1)
        Linked lists are sequential memory, and have a runtime complexity of 0(n)
"""

