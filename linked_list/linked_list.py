"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

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

    def add_to_tail(self, value):
        if self.tail:
            self.tail.set_next(Node(value))
            self.tail = self.tail.get_next()
        else:
            self.head = Node(value)
            self.tail = self.head

    def remove_head(self):
        if self.head:
            removed = self.head.get_value()
            self.head = self.head.get_next()
            if self.head is None or self.head.get_next() is None:
                self.tail = self.head
            return removed

    def contains(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None

        max_value = self.head.get_value()
        current = self.head 
        while current:
            if current.get_value() > max_value: # left side evaluated first
                max_value = current.get_value()
            current = current.get_next()
        return max_value
