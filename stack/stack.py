from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
   """


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size = self.size + 1
#         self.storage.append(value)
#         return value

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size = self.size - 1
#             value = self.storage.pop()
#             return value
            
"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            value = self.storage.remove_tail()
            self.size = self.size - 1
            return value

"""            
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""