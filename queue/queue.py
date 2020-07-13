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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, data):
        self.size += 1
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            self.size -= 1
            to_return = self.head.data
            self.head = self.head.next
            return to_return


queue = Queue()
queue.enqueue(100)
queue.enqueue(101)
queue.enqueue(105)

print(queue.dequeue())
print(queue.dequeue())
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)
#
#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop(0)

