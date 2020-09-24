class Node:
    def __init__(self, value, next_node=None):

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

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.head is None:
            self.tail = new_node

    def add_to_tail(self, value):

        new_node = Node(value)

        if self.head is None and self.tail is None:

            self.head = new_node
            self.tail = new_node

        else:

            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):

        if self.head is None and self.tail is None:

            return None

        if self.head == self.tail:

            value = self.head.get_value()

            self.head = None
            self.tail = None

            return value

        else:

            value = self.tail.get_value()

            current_node = self.head

            while current_node.get_next() != self.tail:

                current_node = current_node.get_next()

            self.tail = current_node

            self.tail.set_next(None)

            return value

    def remove_head(self):

        if self.head is None and self.tail is None:

            return None

        if self.head == self.tail:

            value = self.head.get_value()

            self.head = None
            self.tail = None

            return value

        else:

            value = self.head.get_value()

            self.head = self.head.get_next()

            return value
