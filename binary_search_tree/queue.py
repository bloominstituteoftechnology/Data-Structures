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
from stack import LinkedList

class QueueFromArray:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            first_in_line = self.storage[0]
            self.storage = self.storage[1:]
            self.size -= 1

            return first_in_line

class QueueFromLinkedList:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

class QueueFromStack(object):

    def __init__(self):
        self.size = 0
        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()

    def __len__(self):
        if self.size>0:
            return self.size
        else:
            return 0

    def enqueue(self, item):
        self.in_stack.push(item)
        self.size += 1

    def dequeue(self):
        if not self.in_stack.is_empty():
            #takes off in_stack and puts onto out_stack
            while self.in_stack.size() > 0:
                self.out_stack.push(self.in_stack.pop())
            #removes value
            res = self.out_stack.pop()
            #takes off out_stack and puts back onto in_stack
            while self.out_stack.size() > 0:
                self.in_stack.push(self.out_stack.pop())
            self.size -= 1
            return res


# class Queue(QueueFromArray):
# class Queue(QueueFromLinkedList):
class Queue(QueueFromStack):
    def __init__(self):
        super().__init__() 