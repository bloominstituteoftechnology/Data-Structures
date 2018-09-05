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
        new_tail = Node(value)
        if not self.head:
            self.tail = new_tail
            self.head = new_tail
        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail


    def remove_head(self):
        if not self.head:
            return None

        old_head = self.head.get_value()
        self.head = self.head.get_next()
        self.tail = None
        return old_head

    def contains(self, value):
        read_node = self.head

        while read_node:
            if read_node.get_value() == value:
                return True
            read_node = read_node.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None

        read_node = self.head.get_next()
        max_value = self.head.get_value()

        while read_node:
            read_value = read_node.get_value()
            if read_value > max_value:
                max_value = read_value
            read_node = read_node.get_next()
        return max_value
    
