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
import numpy as np
from singly_linked_list import LinkedList
from singly_linked_list import ListNode

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = np.array([])
        self.storage = LinkedList(None)

    def __len__(self):
        return self.size
    
    def __str__(self):
        print(self.storage)

    def push(self, value):
        # I'm going to assume that I'm pushing something onto the top of the stack
        # self.storage = np.append(self.storage, value)
        self.storage.add_to_tail(value)
        self.size += 1
        return 
        

    def pop(self):
        # I'm going to assume that I'm popping something off the top of the stack
        if self.size == 0:
            return None
        # else:
        #     delvalue = self.storage[-1]
        #     self.storage = self.storage[:-1]
        else:
            tail_value = self.storage.tail.value
            self.storage.remove_tail()
            self.size -= 1
            return tail_value