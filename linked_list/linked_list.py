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
        node = Node(value)
        if self.head:
            self.tail.set_next(node)
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def remove_head(self):
        if self.head:
            head = self.head
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.head = None
                self.tail = None
            return head.value
        else:
            return None

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next_node
        return None

    def get_max(self):
        if self.head:
            current = self.head
            max_value = current.value
            while current:
                if current.value > max_value:
                    max_value = current.value
                    current = current.next_node
                else:
                    current = current.next_node
            return max_value
        else:
            return None
