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

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        '''
        Returns the number of elements in the stack
        '''
        return len(self.storage)

    def push(self, value):
        '''
        Adds a value to the top of the stack
        '''
        self.storage.insert(0, value)

    def pop(self):
        '''
        removes and returns the element at the top of the stack
        '''
        if not self.storage:
            return None

        return self.storage.pop(0)

        
