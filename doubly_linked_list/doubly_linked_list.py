class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        node = ListNode(value)
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node
        else:
            self.next = node

    def insert_before(self, value):
        node = ListNode(value)
        if self.prev:
            temp = self.prev
            node.prev = temp
            self.prev = node
        else:
            self.prev = node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        node = ListNode(value)
        if self.head:
            temp = self.head
            node.next = temp
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def remove_from_head(self):
        if self.head:
            temp = self.head
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return temp.value
        else:
            return None

    def add_to_tail(self, value):
        node = ListNode(value)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def remove_from_tail(self):
        if self.tail:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp.value
        else:
            return None

    def move_to_front(self, node):
        if node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node == self.head:
            self.remove_from_head()
        else:
            node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        pass
