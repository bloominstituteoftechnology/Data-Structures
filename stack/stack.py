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

   ANSWER:
   With a linked list, it is a little trickier when implement normal array methods such as push/pop.
"""

import sys
sys.path.append('./singly_linked_list')
from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __len__(self):
        return self.linked_list.count

    def push(self, value):
        self.linked_list.add_to_tail(value)

    def pop(self):
        if self.linked_list.count > 1:
          return self.linked_list.remove_tail()
        elif self.linked_list.count == 1:
          return self.linked_list.remove_head()
        else:
          pass
