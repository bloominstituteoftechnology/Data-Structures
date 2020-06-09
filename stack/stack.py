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


class ArrStack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        # If storage exists / is populated....
        if self.storage:
            return self.storage.pop()


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """Linked list class"""
    def __init__(self):
        self.first = None
        self.count = 0

    def __len__(self):
        return self.count

    def push(self, value):
        if self.first is None:  # If first entry does not exist...
            self.first = Node(value)  # First entry is the node.
        else:
            # Else, next = first
            node = Node(value, next=self.first)
            self.first = node
        self.count += 1

    def pop(self):
        if self.first is None:  # If first entry doesn't exist...
            return None  # ... return nothing.
        else:  # If it does...
            node = self.first  # node is the first entry
            self.first = self.first.next  # Set the next entry to current.
            self.count -= 1  # Remove the entry from the count
            return node.value  # Return the node

# 3. What is the difference between using an array vs. a linked list when
# implementing a Stack?

# The biggest difference in working with an array vs a linked list when
# implementing a stack is having to manually set the first entry to the next
# entry in .pop().
