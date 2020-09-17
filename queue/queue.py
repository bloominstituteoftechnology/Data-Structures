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
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        current_node = self.head
    
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        if self.head is not None and self.tail is None:
            self.head = new_node
            self.tail = current_node
            self.size += 1
            return
        else:
            self.head = new_node
            self.head.set_next(current_node)
            self.size += 1
            return

    def dequeue(self):
        if self.size == 0:
            return None
        if self.size == 1:
            val = self.head.get_value()
            self.head = None
            self.size -= 1
            return val
        if self.size == 2:
            cur_head = self.head
            val = self.tail.get_value()
            self.tail = cur_head
            self.size -= 1
            return val
        else:
            val = self.tail.get_value()
            cur_node = self.head
            while cur_node.get_next() != self.tail:
                cur_node = cur_node.get_next()
            self.tail = cur_node
            self.tail.set_next(None)
            self.size -= 1
            return val

q = Queue()

print('len', len(q))
q.enqueue(1)
print('len', len(q))
q.enqueue(2)
print('len', len(q))
q.dequeue()
print('len', len(q))
print(q.tail)
            