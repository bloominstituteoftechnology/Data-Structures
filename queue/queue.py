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
# Array Implementation
# class Queue:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             removed = self.storage.pop(0)
#             return removed

# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None

        elif self.head.next is None:
            removed = self.head
            self.head = None
            self.size = 0
            return removed.data

        else:
            removed = self.head
            self.head = self.head.next
            self.size -= 1
            return removed.data
