class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.head.next = self.head
        self.head = new_node

        #[0. 1, 2, 3, 4, 5, None]

    def remove_head(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_tail(self):
        if self.tail is None:
            return

        if self.head == self.tail:
            self.tail = None
            self.tail = None

        if self.head.next is None:
            self.head = None
            self.tail = None

        pointer = self.head
        while pointer.next is not self.tail:
            pointer = pointer.next

        self.tail = pointer

# arr = [1, 2, 3, 4]
# Every Node is a List
# 1 => 1, 2, 3, 4, None
# 2 => 2, 3, 4, None
# 3 => 3, 4, None
# 4 => 4, None
# None is a valid, but empty, value

# A node is a single element in the list
# That single element can be ANYTHING
