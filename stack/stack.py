from singly_linked_list import LinkedList
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
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        # return len(self.storage)
        return self.storage.len()

    def push(self, value):
        # self.storage.append(value)
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.len():
            # last_item = self.storage[self.storage.len() - 1]
            # self.storage.pop()
            # return last_item
            return self.storage.remove_tail()


new_stack = Stack()
