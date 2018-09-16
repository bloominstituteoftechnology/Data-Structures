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
        pass

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass
