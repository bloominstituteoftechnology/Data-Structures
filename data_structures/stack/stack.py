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

# doing the imports
from data_structures.singly_linked_list.singly_linked_list import LinkedList 

class Stack:


    # implementation with a list
    #def __init__(self):
    #    self.size = 0
    #    self.storage = []
#
    # implementation with a linked_list
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    
    # implementation with a list
    #def __len__(self):
    #    # can just use the len method found with python
    #    return len(self.storage)

    # implimentation with a singl linked list
    def __len__(self):
        # using the length value that I have stored in my singly linked list
        return self.size
    
    # implementation with a list
    #def push(self, value):
    #    # putting the element on the top of the stack
    #    # will put on the end of a list
    #    self.storage.append(value)
    #    self.size += 1

    def push(self, value):
        # putting the element on the top of the stack
        # will put on the end of a list
        self.storage.add_to_head(value)
        self.size += 1
    
    # implemenation with a list
    #def pop(self):
    #    # if there is no list then will return None
    #    if self.size == 0:
    #        return None
    #    # removing from the top of the list
    #    self.size -= 1
    #    return self.storage.pop()
##
    def pop(self):
        # if there is no list then will return None
        if self.size == 0:
            return None
        # removing from the top of the list
        self.size -= 1
        return self.storage.remove_head()
#