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
""" class Stack:
    def __init__(self):
        self.storage = list()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop() """

#linked list implementation

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return f"{self.value}"

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        current_node = self.head

        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            self.head = new_node
            self.head.set_next(current_node)
            self.size += 1
    
    def pop(self):
        if self.head is None:
            return None
        if self.size == 1:
            self.size -= 1
            value = self.head.get_value()
            self.head = None
            return value
        else:
            self.size -= 1
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


            


