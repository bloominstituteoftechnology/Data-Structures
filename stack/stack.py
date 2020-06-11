import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

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
# # 1. Array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         if self.storage == []:
#             return None
#         else:
#             return self.storage.pop(0)

# 2. Linked List
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1 # once you "append", you have to update the count

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

# 3. What is the difference between using an array vs. a linked list when implementing a Stack?
# When using a stack, the difference is removing the head. 
# An array can pop the element at the first instance, whereas in a linked list
# other elements main be chained to the first element and therfore those elements will have to be updated