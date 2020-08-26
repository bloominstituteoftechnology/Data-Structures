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
   With an array it will be given block memory because it is all essentially one chunk of data. With a linked list it will be individual nodes that point to the next so the the first node is the only neccessary one to store. 
"""
import time
# from singly_linked_list.singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0)




# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#     def __len__(self):
#         return len(self.storage)
#     def push(self, value):
#         self.storage.add_to_head(value)
#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.remove_head()

n = 100000
stack = Stack()
start = time.time()
for i in range(n):
    stack.push(i)
print("Pushing (to front): ", time.time() - start)
start = time.time()
for i in range(n):
    stack.pop()
print("Popping (from front): ", time.time() - start)
