"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         return self.storage

#     def dequeue(self):
#         if self.__len__() is 0:
#             return None
#         else:
#             return self.storage.pop(len(self.storage) - 1)

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def enqueue(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def dequeue(self):
        self.size -= 1
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value


l = Queue()

print(l.enqueue(100), "Length:", l.__len__())
print(l.enqueue(101), "Length:", l.__len__())
print(l.enqueue(105), "Length:", l.__len__())
print(l.enqueue(4), "Length:", l.__len__())


print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())