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
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head:
            if self.head.get_next() == None:
                head = self.head
                self.head = None
                self.tail = None
                return head.get_value()
            else:
                head = self.head
                self.head = self.head.get_next()
                return head.get_value()
        else:
            return None

    def contains(self, value):
        current_node = self.head
        while current_node:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next()
        return False

    def get_max(self):
        current_node = self.head
        max_value = None
        while current_node:
            if max_value is None or current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.get_next()
        return max_value
