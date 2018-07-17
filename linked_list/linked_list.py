"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        if self.tail is not None:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
        else:
            self.tail = Node(value)
            self.head = self.tail

    def remove_head(self):
        if self.head is not None:
            return_value = self.head.value
            if self.head is self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next_node
            return return_value
        else:
            return None

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next_node
        return False

    def get_max(self):
        if self.head is None:
            return None
        current_node = self.head
        biggest_value = float("-inf")
        while current_node is not None:
            if current_node.value > biggest_value:
                biggest_value = current_node.value
            current_node = current_node.next_node
        return biggest_value
