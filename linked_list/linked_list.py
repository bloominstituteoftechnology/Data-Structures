"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return "Value: {}".format(self.value)

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
        if self.head is None:
            self.head = node
            self.tail = self.head

        elif self.head.get_next is None:
            self.head.set_next(node)
            self.tail = self.head.get_next()
        else:
            self.tail.set_next(node)
            self.tail = self.tail.get_next()

    def remove_head(self):
        if self.head is not None:
            temp = self.head
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.get_next()
            return temp.get_value()
        else:
            return None

    def contains(self, value):
        search = self.head
        while search is not None:
            if search.value == value:
                return True
            else:
                search = search.get_next()
        return False

    def get_max(self):
        search = self.head
        topVal = -10000
        if search is None:
            return None
        while search is not None:
            if search.value > topVal:
                topVal = search.value
            else:
                search = search.get_next()
        return topVal
