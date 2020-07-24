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
class Node:
    def __int__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return 

    def push(self, value): # add to tail
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def pop(self): # remove from tail
        
