from node import Node

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            self.tail = current
            current.set_next(new_node)

    def make_new_head(self, value):
        new_node = Node(value)
        previous_head = self.head
        self.head = new_node
        self.head.set_next(previous_head)

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value.value

    def remove_from_tail(self):
        if not self.head:
            return None
        else:
            previous = self.head
            current = self.head
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            self.tail = previous
            previous.set_next(None)
            return current.get_value()
