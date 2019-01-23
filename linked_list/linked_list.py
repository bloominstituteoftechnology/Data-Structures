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
        if self.head == None:
            return ("empty list")
        new_head = self.head.next_node
        value = self.head
        del(self.head)
        self.head = new_head
        return value

    def contains(self, value):
        curr_node = self.head
        while True:
            if curr_node is None:
                return False
            elif curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next_node

    def get_max(self):
        curr_node = self.head
        max_number = 0
        while True:
            if curr_node is None:
                return max_number
            elif curr_node.value > max_number:
                max_number = curr_node.value
            else:
                curr_node = curr_node.next_node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)

    def dequeue(self):
        value = self.storage.head.value
        self.storage.remove_head()
        return value

    def len(self):
        curr_node = self.storage.head
        iterations = 0
        while True:
            if curr_node is None:
                return iterations
            else:
                curr_node = curr_node.next_node
                iterations += 1
