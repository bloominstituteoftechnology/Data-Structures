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
        if self.tail is not None:
            self.tail.set_next(node)
        else:
            self.head = node
        self.tail = node

    def remove_head(self):
        # Check to see if none
        if self.head is not None:
            # create temp variable
            new_head = self.head.next_node
            if new_head is None:
                self.tail = None
            prev_head = self.head.get_value()
            # New head becomes head
            self.head = new_head
            return prev_head
        else:
            self.tail = None
            return None

    def contains(self, value):
            # Set the current node to the head
        curr_node = self.head

        while True:
            # If the node is null, return False
            if curr_node is None:
                return False
            # Else, if the node's value matches the query value, return True
            elif curr_node.get_value() == value:
                return True
            else:
                curr_node = curr_node.next_node

        # Otherwise, set the current node to the tail and start from

    def get_max(self):
        curr_node = self.head
        maxNode = -float("inf")
        if curr_node is None:
            return None

        while curr_node is not None:
            if curr_node is not None:
                if curr_node.get_value() > maxNode:
                    maxNode = curr_node.get_value()
            else:
                pass
            curr_node = curr_node.next_node
        return maxNode
