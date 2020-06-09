class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

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
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.tail is None:
            return None
        value = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
        return value

    def remove_head(self):
        if self.head is None:
            return None
        value = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False
        current = self.head 
        while current is not None:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if self.head is None:
            return None
        max_so_far = self.head.get_value()
        current = self.head.get_next()
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()
            current = current.get_next()
        return max_so_far