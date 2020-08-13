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
An array consumes contiguous memory 
 locations allocated at compile time,
A linked list is allocated by accessing the
data structure, where each element can be accesed only in particular order.
Stretch: What if you could only use 
instances of your Stack class to implement the Queue?
What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
#     1. Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        # add to queue
        return self.storage.append(value)

    def dequeue(self):
        if len(self.storage) >= 1:
            return self.storage.pop()
        
        
class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def get_length(self):
        return self.length    

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

 

    def remove_tail(self):
        # (2+ node) if tail == None ; return None
        # else assign value --> to tail value
        # assign tail to that "next" value
        # adjust node length
        # return value

        if self.tail is None:
            return None

        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        else:
            value = self.tail.get_value()
            self.tail = value.get_next()
            self.length -= 1
            return value
        
        
    def remove_head(self):
        # empty linkedlist
        if self.head is None:
            return None

        # list with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value

        # list with 2+ Nodes
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value    
 
        
class Queue:
# 2. Re-implement the Queue class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Queue tests pass.
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.get_length()

    def enqueue(self, value):
        # add to queue "tail"
        self.size =+ 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # remove from queue "head"
        if self.size >= 1:
            self.size -= 1
        return self.storage.remove_head()
