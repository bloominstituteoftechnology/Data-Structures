# TODO a class that represents the individual elements in our LL

class Node:
    def __init__(self, value, next_node):
        self.value = value
        self. next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            # update head & tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next_node(self.head)
            # update head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # TODO

    def remove_head(self):
        # cases to consider?
        # empty LinkedList
        if self.head is None:
            return None
        # else, return value of old head
        # list with 2 or more elements - return value of the old head
        else:
            self.head = self.head.get_next_node()

    def remove_tail(self):
        # TODO

    def contains(self, value):
        # TODO:

    def get_max(self, value):
        # TODO:
