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
        new_index = Node(value)
        if self.tail is not None:
            self.tail.set_next(new_index)
        else:
            self.head = new_index
        self.tail = new_index

    def remove_head(self):
        # self.head = None
        if self.head is not None:
            new = self.head.next_node()
            del self.head
            self.head = new

    def contains(self, value):
        current = self.head
        while 1:
            if current == None:
                return False
            elif current == value:
                return True
            else:
                current = current.next_node()

    def get_max(self):
        max_val = 0
        current = self.head
        for i in range(1):
            if max_val < current:
                max_val = current.value
            else:
                current = current.next_node()

