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
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_text): 
        self.next = new_text

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value)

        if self.tail is None and self.tail is None: 
            # in a one-element linked list, what should head and tail be referring to?
            # have both head and tail reffering to the single node.
            self.head = new_node
            # set the new node to be the tail.
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = head
            self.tail = None
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return 

        if self.head == self.tail:
            # store the node so we can remove the value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        else: 
            val = self.tail.get_value()
            current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()


        self.tail = current
        self.tail.set_next(None)
        self.tail = current
        return val


class Queue:
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
            return
        else:
            removedValue = self.storage.remove_head()
            self.size -= 1
            return removedValue
