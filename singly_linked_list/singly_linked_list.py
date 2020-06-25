class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return('Empty list')
        else:
            current = self.head
            string = f'[{self.head.value}'
            while current.next is not None:
                string += f', {current.next.value}'
                current = current.next
            string += ']'
            return string

    def add_to_tail(self, value):
        if self.tail is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def remove_head(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value

    def get_max(self):
        if self.head is None:
            return None
        else:
            current = self.head
            max_value = self.head.value
            while current.next is not None:
                current = current.next
                max_value = max((max_value, current.value))
            return max_value