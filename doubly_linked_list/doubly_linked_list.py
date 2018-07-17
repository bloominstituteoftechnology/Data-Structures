class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
       self.next = ListNode(value, prev=self)
       return self.next

    def insert_before(self, value):
       self.prev = ListNode(value, next=self)
       return self.prev

    def delete(self):
        if self.next:
            self.next.prev = self.get_prev()
        if self.prev:
            self.prev.next = self.get_next()
        del(self)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head:
            self.head = self.head.insert_before(value)
        else:
            self.head = ListNode(value)
            self.tail = self.head

    def remove_from_head(self):
        removed = self.head.get_value()
        self.head.delete()
        return removed

    def add_to_tail(self, value):
        if self.tail:
            self.tail = self.tail.insert_after(value)
        else:
            self.tail = ListNode(value)
            self.head = self.tail

    def remove_from_tail(self):
        removed = self.tail.get_value()
        self.tail.delete()
        return removed

    def move_to_front(self, node):
        current = self.head
        while current:
            if current == node:
                value = node.get_value()
                self.delete(node)
                self.add_to_head(value)
            current = current.get_next()

    def move_to_end(self, node):
        current = self.head
        while current:
            if current == node:
                value = node.get_value()
                self.delete(node)
                self.add_to_tail(value)
            current = current.get_next()

    def delete(self, node):
        node.delete()
