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
        newNode = Node(value)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.set_next(newNode)
            self.tail = newNode

    def remove_head(self):
        removed = self.head
        self.head = self.head.get_next()
        return removed.get_value()

    def contains(self, value):
        nextValue = self.head
        while (nextValue != None):
            if nextValue.get_value() == value:
                return True
            else:
                nextValue = nextValue.get_next()
        return False

    def get_max(self):
        pass
