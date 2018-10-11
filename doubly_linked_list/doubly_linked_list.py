class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        new_node = ListNode(value, self, self.next)
        if self.next is not None:
            self.next, self.next.prev = new_node
        else:
            self.next = new_node
        return new_node

    def insert_before(self, value):
        new_node = ListNode(value, self.prev, self)
        if self.prev is not None:
            self.prev, self.prev.next = new_node
        else:
            self.prev = new_node
        return new_node

    def delete(self):
        if self.prev is not None:
            self.prev.next = self.next if self.next is not None else None
        if self.next is not None:
            self.next.prev = self.prev if self.prev is not None else None


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if self.head is not None:
            self.head = self.head.insert_before(value)
        else:
            self.head, self.tail = ListNode(value)

    def remove_from_head(self):
        d_node = self.head
        d_node.delete()
        self.head = d_node.next
        return d_node.value

    def add_to_tail(self, value):
        if self.tail is not None:
            self.tail = self.tail.insert_after(value)
        else:
            self.head, self.tail = ListNode(value)

    def remove_from_tail(self):
        d_node = self.tail
        d_node.delete()
        self.tail = d_node.prev
        return d_node.value

    def move_to_front(self, node):
        node.delete()
        self.head.prev, node.next, self.head = node, self.head, node

    def move_to_end(self, node):
        node.delete()
        self.tail.next, node.prev, self.tail = node, self.tail, node

    def delete(self, node):
        node.delete()
