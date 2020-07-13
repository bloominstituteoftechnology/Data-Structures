# Implement the Stack and Queue classes using built-in Python lists 
# and the Node and LinkedList classes you created during the 
# Module 1 Guided Project.

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

# Should have the methods: push, pop, and len.

# push adds an item to the top of the stack.
# pop removes and returns the element at the top of the stack
# len returns the number of elements in the stack.

# Using built-in python lists
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        """Adds an item to the top of the stack"""
        self.storage = [value] + self.storage
        return self.storage

    def pop(self):
        """Removes and returns the element at the top of the stack"""
        top = self.storage[0]
        self.storage.remove(top)
        new_top = self.storage[0]
        return new_top


# # Using Node and LinkedList classes
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?

#     def __len__(self):
#         pass

#     def push(self, value):
#         pass

#     def pop(self):
#         pass