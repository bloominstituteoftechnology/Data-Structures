class Node:
    # Stores two pieces of data:
    # 1. Value
    # 2. The Next Node

    # Methods
    # 1. Get value
    # 2. Set value
    # 3. Get next
    # 4. Set next
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    # 1. Ref to the head Node
    # 2. Ref to the tail Node

    def __init__(self):
        self.head = None
        self.tail = None

    # Behavior
    # 1. Append

    def add_to_tail(self, value):
        new_tail = Node(value)
        if not self.head:               # If no head
            self.head = new_tail
        else:                               # If there is head
            self.tail.set_next(new_tail)
        self.tail = new_tail

    # 2. Prepend

    def add_to_head(self, value):
        new_head = Node(value)          # Create the new head
        new_head.set_next(self.head)    # Old head becomes the next of new head
        if self.head is None:           # If there was no item in the list;
            self.tail = new_head        # Then head and tail becomes the same value
        self.head = new_head            # Set new head as head anyways

    # 3. Remove Head

    def remove_head(self):

        if not self.head:  # No item
            return None

        if not self.head.get_next():  # One Item
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        value = self.head.get_value()  # Multiple items
        self.head = self.head.get_next()
        return value

    # 4. Remove Tail

    def remove_tail(self):
        if not self.head:  # No item
            return None

        if self.head is self.tail:  # One item
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head  # Multiple items

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value

    # 5. Contains?

    def contains(self, value):
        if not self.head:  # No item
            return False

        current = self.head  # If there is at least one item

        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    # 6. Get Maximum

    def get_max(self):
        if not self.head:  # No item
            return None

        max_value = self.head.get_value()
        current = self.head.get_next()

        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value
