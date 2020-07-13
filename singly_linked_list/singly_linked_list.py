class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def contains(self, value) -> bool:

        node = self.head

        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False

    def remove_head(self):


        if self.head is None:
            return
        else:
            value = self.head.value

            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next

            return value

    def get_max(self):
        max = None
        node = self.head

        while node is not None:
            if max is None:
                max = node.value
            elif node.value > max:
                max = node.value

            node = node.next

        return max
