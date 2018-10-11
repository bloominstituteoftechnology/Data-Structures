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
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = self.tail.next_node

    def remove_head(self):
        if self.head == None:
            return None
        elif self.head.next_node == None:
            node = self.head
            self.head = None
            self.tail = None
            return node.value
        else:
            node = self.head
            self.head = self.head.next_node
            node.next_node = None
            return node.value

    def contains(self, value):
        if self.head == None:
            return False
        else:
            node = self.head
            while node != None:
                if node.value == value:
                    return True
                node = node.next_node
            return False

    def get_max(self):
        if self.head == None:
            return None
        else:
            node = self.head
            max = 0
            while node != None:
                if max < node.value:
                    max = node.value
                node = node.next_node
            return max
