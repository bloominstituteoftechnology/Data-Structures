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
        last = self.head
        while (last.next_node):
            last = last.next_node
        last.next_node = new_node

    def remove_head(self):
        node_to_remove = self.head
        if node_to_remove is not None:
            self.head = node_to_remove.next_node
            node_to_remove = None
            return self.head

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def get_max(self):
        max_value = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node
        return max_value
