"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
import math


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
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def remove_head(self):
        if self.head:
            head = self.head
            self.head = self.head.get_next()
            self.tail = None
            return head.value

    def contains(self, value):
        first_node = self.head
        while first_node != None:
            if first_node.value == value:
                return True
            else:
                first_node = first_node.next_node
        return False

    def get_max(self):
        first_node = self.head
        max_value = float("-inf")
        if first_node == None:
            return None
        while first_node != None:
            if first_node.value > max_value:
                max_value = first_node.value
            else:
                first_node = first_node.next_node
        return max_value
