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
        new_node = Node(value, None)
        # If empty list
        if not self.head:
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # current tail references new node
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # If empty list
        if not self.head:
            return None
        # if head has no next, list has a single node
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        # Otherwise, remove current node
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value