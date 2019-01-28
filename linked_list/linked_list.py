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
        # create new node
        node = Node(value)
        # if the LL is not empty
        if self.tail is not None:
            self.talk.set_next(node)
        else:
            # if it is empty, set the new node to the head
            self.head = node
        # set the LL's tail to the new node
        self.tail = node

    def remove_head(self):
        # set the head nodes next node value to a temp var
        new_head = self.head.next_node
        # delete the head node
        del(self.head)
        # then set head to that temp
        self.head = new_head

    def contains(self, value):
        pass

    def get_max(self):
        pass
