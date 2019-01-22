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
        #  Create a new node
        node = Node(value)
        #  If the Linked List is not empty
        if self.tail is not None:
            # Then set the tail's next to the new node
            self.tail.set_next(node)
        else:
            # If it is empty, set the new node to the head
            self.head = node
        # Set the Linked List's tail to the new node
        self.tail = node

    def remove_head(self):
        # Check if the head is None
        if self.head is not None:
            # Set the head nodes next node value to a temp var
            new_head = self.head.next_node
            # Delete the head node
            del(self.head)
            # Set new pointer
            self.head = new_head
            # Set new head to that temp

    def contains(self, value):
        # set current node to the head
        # 1. if the node is null, return false
        # 2. else if the node's value matches the query value, return true
        # 3. otherwise set the current node to the tail start from step 2

    def get_max(self):
        pass
