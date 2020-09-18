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
# list impiementation
""" class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop() """

 # linked list implementation

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return f"{self.value}"

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        current_node = self.rear
    
        if self.rear is None and self.front is None:
            self.rear = new_node
            self.front = new_node
            self.size += 1
            return
        if self.rear is not None and self.front is None:
            self.rear = new_node
            self.front = current_node
            self.size += 1
            return
        else:
            self.rear = new_node
            self.rear.set_next(current_node)
            self.size += 1
            return

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size == 1:
            val = self.rear.get_value()
            self.rear = None
            self.size -= 1
            return val
        if self.size == 2:
            cur_rear = self.rear
            val = self.front.get_value()
            self.front = cur_rear
            self.size -= 1
            return val
        else:
            val = self.front.get_value()
            cur_node = self.rear
            while cur_node.get_next() != self.front:
                cur_node = cur_node.get_next()
            self.front = cur_node
            self.front.set_next(None)
            self.size -= 1
            return val



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.rear)