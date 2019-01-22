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
        if self.head is not None:
            if self.head.next_node is not None:
                deleted_value = self.head.get_value()
                new_head = self.head.next_node
                del(self.head)
                self.head = new_head
                return deleted_value
            else:
                deleted_value = self.head.get_value()
                self.head = None
                self.tail = None
                return deleted_value

    def contains(self, value):
        curr_node = self.head
        while True:
            if curr_node == None:
                return False
            elif curr_node.get_value() == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        if self.head is not None:
            curr_node = self.head
            if curr_node.next_node is not None:
                next_node = curr_node.next_node
                while True:
                    if curr_node.get_value() <= next_node.get_value():
                        curr_node = next_node
                    else:
                        return curr_node.get_value()
            else:
                return curr_node.get_value()
        else:
            return None
