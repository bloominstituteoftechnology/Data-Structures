class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        self.next = ListNode(value, self, self.next)
        if self.next.next:
            self.next.next.prev = self.next

    def insert_before(self, value):
        self.prev = ListNode(value, self.prev, self)
        if self.prev.prev:
            self.prev.prev.next = self.prev

    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode(1)
        self.tail = self.head

    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def remove_from_head(self):
        return_value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return return_value

    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(value)
            self.head = self.tail

    def remove_from_tail(self):
        return_value = self.tail.value
        if self.tail is self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return return_value

    def move_to_front(self, node):
        self.add_to_head(self.delete(node))

    def move_to_end(self, node):
        self.add_to_tail(self.delete(node))

    def delete(self, node):
        if self.head is node:
            self.head = node.next
        if self.tail is node:
            self.tail = node.prev
        return node.delete()
