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
        self.length = 0

    def add_to_tail(self, value):
        # creates a new node and assign it as the head of the list since length is 0
        # when run again would assign next on previous item and set default next to none
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next_node = newNode
            self.tail = newNode
            self.length += 1

    def remove_head(self):
        if self.head is not None:
            value = self.head.value
            if self.head.next_node is not None:
                newhead = self.head.next_node
                self.length -= 1
                self.head = newhead
                return value
            elif self.head.next_node is None or 'next_node':
                self.head = None
                self.tail = None
                self.length -= 1
                return value

    def contains(self, value):
        if self.head == None:
            return False
        current = self.head
        while (current.next_node):
            if current.value == value:
                return True
            current = current.next_node
        if current.value == value:
            return True
        return False

    def get_max(self):
        if self.head == None:
            return None
        current = self.head
        total = self.head.value
        while current:
            if current.value > total:
                total = current.value
                current = current.get_next()
            else:
                current = current.get_next()
        return total
