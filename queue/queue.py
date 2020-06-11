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
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def __len__(self):
        return self.count

    def enqueue(self, value):
        if self.first is None:
            node = Node(value)
            self.first = node
            self.last = node
        else:
            node = Node(value)
            self.last.next = node
            self.last = node
        self.count += 1
    
    def dequeue(self):
        if self.first is None:
            return None
        elif self.first.next is None:
            node = self.first
            self.first = None
            self.last = None
            self.count -= 1
            return node.value
        else:
            node = self.first
            self.first = self.first.next
            self.count -= 1
            return node.value

class ListQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage:
            return self.storage.pop(0)
