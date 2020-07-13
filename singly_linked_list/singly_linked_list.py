class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def contains(self, item):
        current = self.head

        while current is not None:
            if current.get_value() == item:
                return True
            else:
                current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None

        current = self.head
        max = 0

        while current is not None:
            if current.get_value() > max:
                max = current.get_value()
            current = current.get_next()

        return max

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None:
            return

        current = self.head

        while current.get_next() is not None and current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    def remove_head(self):
        if self.head is None:
            return

        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
