
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
'''
class Queue:
    def __init__(self, storage=[]):
        self.size = 0
        self.storage = storage 
    
    def __str__(self):
        return f'{self.storage}'

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop(0)
'''
# testarr = []
# test = Queue(testarr)
# test.enqueue(1)
# test.enqueue(2)
# test.enqueue(3)
# test.dequeue()
# print(test)



class Queue:
    def __init__(self):
        self.size = 0
        self.data = LinkedList()
    def __str__(self):
        return f'{self.data}'
    def __len__(self):
        return self.size
    def enqueue(self,value):
        self.data.add_to_tail(value)
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            return None
        else: 
            self.size -= 1
            return self.data.remove_from_head()

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next
    def __str__(self):
        return f'{self.value}'
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        return f'{self.head}'
    def add_to_tail(self,data):
        new_node = Node(data)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_from_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: 
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
        return data
    
    def remove_from_head(self):
        if self.head is None:
            return None
        data = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return data
