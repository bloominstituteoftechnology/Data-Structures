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
# Array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.storage == []:
#             return None
#         else:
#             last_index = len(self.storage) - 1
#             self.size -= 1
#             return self.storage.pop(last_index)

# Linked List
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass