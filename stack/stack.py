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

# 1. Implement the Stack class using an array as the underlying storage structure.
#    Make sure the Stack tests pass.

# class Stack:
#     """Array as the underlying storage structure"""
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         if self.size != 0:
#             self.size -= 1
#             return self.storage.pop()


# 2. Re-implement the Stack class, this time using the linked list implementation
#    as the underlying storage structure.

from singly_linked_list import LinkedList
class Stack():
    """Linked list as the underlying storage structure"""
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_tail()


"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   Using an array is easier when implementing a Stack, because we just
   have to add an element at the end of the array, or delete the last element.
   If using a linked list, we have to allocate a new adrress to the tail
   besides changing the pointer of the last element
"""
