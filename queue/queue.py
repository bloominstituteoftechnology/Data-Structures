"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as
   the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances
         of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from DataStructures.singly_linked_list.singly_linked_list import LinkedList
from DataStructures.stack.stack import Stack


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            pop = self.storage.pop(0)
            self.size -= 1
            return pop


class LLQueue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.count

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()

# Stretch


class StackQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.size == 0:
            return None
        else:
            while self.stack1.size > 1:
                self.stack2.push(self.stack1.pop())
            temp = self.stack1.pop()
            while self.stack2.size > 0:
                self.stack1.push(self.stack2.pop())
            return temp

    def __len__(self):
        return self.stack1.size
