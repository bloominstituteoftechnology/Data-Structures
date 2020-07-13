from singly_linked_list import Node, LinkedList


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

# Stack class implemented with a Python list:


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size = self.size + 1
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            print("There is nothing to remove.")
        else:
            popped = self.storage.pop(self.size - 1)
            self.size = self.size - 1
            return popped


# Stack class implemented with a Python linked list:

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.storage.length()

#     def push(self, value):
#         self.storage.add_to_tail(value)
#         self.size = self.size + 1

#     def pop(self):
#         if self.size > 0:
#             value = self.storage.tail.get_value()
#             self.storage.remove_tail()
#             self.size = self.size - 1
#             return value
#         else:
#             return None
