from singly_linked_list import Node, LinkedList

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

# # Using built-in python lists
# class Stack:
#     """Array implementation of Stack class"""
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         """Adds an item to the top of the stack"""
#         self.storage = [value] + self.storage
#         self.size = len(self.storage)
#         return self.storage

#     def pop(self):
#         """Removes and returns the element at the top of the stack"""
#         # if empty
#         if self.size == 0:
#             return None
#         else:
#             top = self.storage[0]
#             self.storage.remove(top)
#             self.size = len(self.storage)
#             return top


# Using Node and LinkedList classes
class Stack:
    """Object-oriented implementation of Stack class with Node and
    LinkedList"""
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count
        return count

    def push(self, value):
        """Adds an item to the top of the stack"""
        self.storage.add_to_head(value)
        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count

    def pop(self):
        """Removes and returns the element at the top of the stack"""
        # if empty
        if self.size == 0:
            return None
        else:
            top = self.storage.head.get_value()
            self.storage.remove_head()
            return top

        count = 0
        current = self.storage.head
        # loop through to count "heads"
        while current:
            current = current.get_next()
            count += 1
        self.size = count

if __name__ == "__main__":
    my_stack = Stack()

    breakpoint()