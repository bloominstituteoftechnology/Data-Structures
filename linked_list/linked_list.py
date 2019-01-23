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
        elif not self.head.next_node:
            self.head.set_next(new_node)
        else:
            self.tail.set_next(new_node)
        self.tail = new_node

    def remove_head(self):
        old_head = None
        if self.head is not None:
            old_head = self.head
            del(self.head)
            self.head = old_head.next_node

            if self.head is None:
                self.tail = None

            return old_head.value

    def contains(self, value):
        curr_node = self.head
        while True:
            if curr_node is None:
                return False
            elif curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        max_val = float("-inf")
        curr_node = self.head
        while True:
            if curr_node is None:
                return None

            if curr_node.value > max_val:
                max_val = curr_node.value

            if curr_node.next_node == None:
                return max_val
            else:
                curr_node = curr_node.next_node
