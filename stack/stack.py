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

   For an array, it is keeping all of the memory kind of together as in, when you add things to an array,
   during compile time it would have to reference that array as a whole... VS. a linked list where,
   the memory is assigned and you can access the data by pointing to certain spots in memory. This happens at runtime.

   (Don't know if that's a clear explanation but it's what kind of makes sense to me.)
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size +=1
        return self.storage

    def pop(self):
        if self.size == 0:
            return None
        else:
            value = self.storage.pop()
            self.size -= 1
        return value
