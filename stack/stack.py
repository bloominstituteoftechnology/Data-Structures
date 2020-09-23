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

from singly_linked_list import Node, LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else:
            removed_node = self.storage.remove_tail()
            self.size -= 1
            return removed_node

    def __len__(self):
        return self.size

# stack = Stack()

# stack.push(4)
# stack.push(45)
# stack.push(5)
# print(stack.__len__())
# stack.pop()
# print(stack.__len__())
