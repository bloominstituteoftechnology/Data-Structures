class ListNode:
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        node = ListNode(value)
        if self.next is None:
            self.next = node
            node.prev = self
        else:
            node.prev = self
            node.next = self.next
            self.next = node
            node.next.prev = node

    def insert_before(self, value):
        node = ListNode(value)
        if self.prev is None:
            self.prev = node
            node.next = self
        else:
            node.next = self
            node.prev = self.prev
            self.prev = node
            node.prev.next = node

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.value = None
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def add_to_head(self, value):
        new_head = ListNode(value=value)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def remove_from_head(self):
        head = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return head

    def add_to_tail(self, value):
        new_tail = ListNode(value=value)
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_tail
            new_tail.prev = current
            self.tail = new_tail

    def remove_from_tail(self):
        if self.head is None:
            return None
        else:
            tail = self.tail.value
            current = self.head
            while current.next is not None:
                current = current.next
            current.prev.next = None
            self.tail = current.prev
            current.prev = None
        return tail

    def move_to_front(self, node):
        if self.head is None: return None
        current = self.head
        while current is not None:
            if current == node:
                self.delete(current)
                self.add_to_head(node.value)
            current = current.next

    def move_to_end(self, node):
        if self.head is None: return None
        current = self.head
        while current.next is not None:
            if current == node:
                self.delete(current)
                self.add_to_tail(node.value)
            current = current.next

    def delete(self, node):
        current = self.head

        while current is not None:
            if current == node:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    current.next.prev = None
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                    current.prev.next = None
            current = current.next