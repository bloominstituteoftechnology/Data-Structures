class Node:
    def __init__(self, value=None, next_node=None):
        # node value
        self.value = value
        # reference to next node
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

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        # add new_node to the self.head
        self.head = new_node
        # if self.length == 0, then the tail becomes the head
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # list with no data:
        if self.head is None:
            return None
        # list with only 1 Node:
        elif self.head == self.tail:
            value = self.head.get_value()
            # "removes" head and tail, since list will be empty
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # list with 2+ Nodes:
        else:
            value = self.head.get_value()
            # "removes" current head, and next_node becomes new head
            self.head = self.head.get_next()
            self.length -= 1
            return value

    def remove_tail(self):
        # list with no data:
        if self.head is None:
            return None
        # list with only 1 Node:
        elif self.head == self.tail:
            value = self.tail.get_value()
            # "removes" head and tail, since list will be empty
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # list with 2+ Nodes:
        else:
            value = self.tail.get_value()
            self.tail = None
            self.length -= 1
            return value


