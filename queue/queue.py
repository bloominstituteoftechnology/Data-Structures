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
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __str__(self):
        if self.size == 0:
            return 'the Queue is empty'
        n = 0
        output = ''
        while n < self.size:
            output += f'[{self.storage[n]}]'
            n += 1
        return output

    def __len__(self):
        if self.size == 0:
            return 0
        else:
            return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        value = self.storage[0]
        self.storage.pop(0)
        self.size -= 1
        return value

#     def enqueue(self, value):
#         self.storage.ad_to_tail(value)
#         self.size +=1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         self.size -=1
#         return self.storage.remove_head
#Implementing using linked list
