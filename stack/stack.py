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
from linked_list_day_1 import LinkedList 
from collections import deque 

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = deque()
       # self.storage = LinkedList()
    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
      #  self.storage.add_to_end(value)
    def pop(self):
        if self.storage:
            return self.storage.pop()
           #return self.storage.remove_from_head()
        else:
            return None 


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#        # return len(self.storage)
#        return self.size 

#     def push(self, value):
#         self.storage.add_to_end(value)
#         self.size += 1

#     def pop(self):
#         if (self.size > 0):
#          # return self.storage.popleft()
          
#           self.size -= 1
#           return self.storage.remove_from_head() 

#         else:
#           return None 