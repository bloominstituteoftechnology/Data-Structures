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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is not None:
            value = self.head.get_value()
            if self.head.get_next() is not None:
                self.head = self.head.get_next()
            else:
                self.head = None
                self.tail = None
            return value

    def contains(self, value):
        node = self.head
        while node is not None:
            if node.get_value() == value:
                return True
            node = node.get_next()
        return False

    def get_max(self):
        max = float('-inf')
        node = self.head
        if node is not None:
            while node is not None:
                if node.get_value() > max:
                    max = node.get_value()
                node = node.get_next()
            return max
        return None
