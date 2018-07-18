class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)

        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def remove_from_head(self):
        if not self.head:
            if not self.tail:
                return None
            return self.remove_from_tail()
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return current_head.value

    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value, self.head, None)
        elif not self.head:
            self.head = self.tail
            self.tail = ListNode(value, self.head, None)
            self.head.next = self.tail
        else:
            self.tail = ListNode(value, self.head, None)
            self.tail.prev.next = self.tail

    def remove_from_tail(self):
        if not self.tail:
            if not self.head:
                return None
            return self.remove_from_head()
        else:
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return current_tail.value

    def move_to_front(self, node):
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
        self.add_to_tail(value)

    def delete(self, node):
        node.delete()
