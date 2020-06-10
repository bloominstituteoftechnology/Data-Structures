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

# 1. Implement the Stack class using an array as the underlying storage structure.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self) > 0:
#             # There are elements in the array. pop the last one.
#             return self.storage.pop()
#         else:
#             return None

# 2. Re-implement the Stack class, this time using the linked list implementation
class Node: 
    def __init__(self, value = None, next_node = None ):
        self.value = value
        self.next_node = next_node 

class Stack:
    def __init__(self):
        self.size = 0
        self.first_node = None
        self.last_node = None

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)

        if self.first_node == None:
            # First element 
            self.first_node = new_node
            self.last_node = new_node
            return 

        self.last_node.next_node = new_node
        self.last_node = new_node

    def pop(self):
        if self.size == 0:
            return None

        node_to_pop = self.last_node
        current_node = self.first_node

        if node_to_pop != current_node:
            while current_node.next_node != node_to_pop:
                current_node = current_node.next_node

        current_node.next_node = None
        self.last_node = current_node
        self.size -= 1

        if self.size == 0:
            self.first_node = None

        return node_to_pop.value
