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
#class Stack:
#    """Array (a.k.a. list) implementation of Stack data structure"""
#
#    def __init__(self):
#        """Initialize array-based Stack class"""
#
#        self.size = 0
#        self.storage = []
#
#    def __len__(self):
#        """Return length of Stack class"""
#
#        self.size = len(self.storage)
#        return self.size
#
#    def push(self, value):
#        """Add an element to initialized Stack class"""
#
#        self.storage.append(value)
#
#    def pop(self):
#        """Remove most recently added element from Stack class"""
#
#        if self.storage.__len__() == 0:
#            return None
#        else:
#            return self.storage.pop(-1)

from singly_linked_list import LinkedList 

class Stack():
    """Singly-linked list implementation of Stack data structure"""

    def __init__(self):
        """Initialize array-based Stack class"""

        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        """Return length of Stack class"""

        return self.size

    def push(self, value):
        """Add an element to initialized Stack class"""

        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        """Remove most recently added element from Stack class"""
        
        if self.__len__() == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


