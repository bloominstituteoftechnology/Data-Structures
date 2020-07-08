class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        node = Node(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_to_head(self, value):
        node = Node(value)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def remove_head(self):
        if self.head is None:
            return None
        value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return value

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_max(self):
        if self.head is None:
            return None

        max = self.head.value
        current = self.head
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max
