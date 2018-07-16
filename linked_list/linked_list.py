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
        if self.head is not None:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
        else:
            self.tail = Node(value)
            self.head = self.tail

    def remove_head(self):
        if self.head is not None:
            head = self.head.value
            self.head = self.head.next_node
            return head
        else:
            return None

    def contains(self, target):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target:
                return True
            else:
                current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        current_node = self.head
        current_max = current_node.value
        while current_node is not None:
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next_node
        return current_max
