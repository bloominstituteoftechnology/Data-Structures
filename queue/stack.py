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

from singly_linked_list import LinkedList

stack = LinkedList()
# arr = []


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = stack

    def __len__(self):
        return self.size

    def push(self, value):
        stack.add_to_head(value)
        self.size += 1
        # arr.append(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return stack.remove_head()

        # end = len(arr)
        # if len(arr) > 0:
        #     value = arr[end]
        #     arr.remove(end)
        #     return value
        # else:
        #     return None
