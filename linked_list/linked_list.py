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
        if self.tail is not None:
            self.tail.set_next(new_node)
        if self.head is None:
            self.head = new_node
        self.tail = new_node

    def remove_head(self):
        old_head = self.head
        return_value = None
        if self.head is not None:
            if self.head == self.tail:
                return_value = old_head.get_value()
                self.head = None
                self.tail = None
            else:
                new_head = old_head.get_next()
                self.head = new_head
                return_value = old_head.get_value()
        return return_value

    def contains(self, value):
        found = False
        if self.head is not None:
            current = self.head
            if self.head == self.tail:
                if self.head.get_value() == value:
                    found = True
            else:
                while current and found is False:
                    if current.get_value() == value:
                        found = True
                    else:
                        current = current.get_next()
        return found

    def get_max(self):
        max = None
        if self.head is not None:
            current = self.head
            if self.head == self.tail:
                max = self.head.get_value()
            else:
                while current:
                    if max is None or current.get_value() > max:
                        max = current.get_value()
                    current = current.get_next()
        return max
