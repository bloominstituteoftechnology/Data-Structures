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
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None and self.tail is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        val = self.head.get_value()
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        if self.head is None:
            return

        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        val = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return val

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.get_value()

        current = self.head.get_next()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()

            current = current.get_next()
        return max_value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        return None
