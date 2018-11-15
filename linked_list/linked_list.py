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
        next_node = Node(value)

        if not self.head:
            self.head = next_node
            self.tail = next_node

        else:
            self.tail.set_next(next_node)
            self.tail = next_node

    def remove_head(self):
        if self.head == None and self.tail == None:
            return None

        if self.head.next_node != None:
            val = self.head.value
            self.head = Node(self.head.next_node)
            self.tail = Node(self.head.value)
            return val

        else:
            val = self.head.value
            self.head = None
            self.tail = None
            return val

    def contains(self, value):
        if self.head == None and self.tail == None:
            pass
        else:
            if self.head.value == value or self.head.next_node == value or self.tail.value == value:
                return True
            else:
                return False

    def get_max(self):
        temp = self.head
        max_value = None
        while temp:
            if max_value is None or temp.get_value() > max_value:
                max_value = temp.get_value()
            temp = temp.get_next()
        return max_value
