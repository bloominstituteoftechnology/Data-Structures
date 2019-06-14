"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointed to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is pointed to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        newhead = ListNode(value)
        newhead.next = self.head
        if self.head:
            self.head.prev = newhead
        self.head = newhead
        if not self.tail:
            self.tail = newhead
        self.length += 1

    def remove_from_head(self):
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return value

    def add_to_tail(self, value):
        newnode = ListNode(value)
        if not self.head and not self.tail:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.length += 1

    def remove_from_tail(self):
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
        self.length -= 1
        return value

    def move_to_front(self, node):
        if node == self.tail:
            self.tail = node.prev
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node == self.head:
            self.head = node.next
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.length -= 1

    def get_max(self):
        current = self.head
        maxval = current.value
        current = current.next
        while current:
            if current.value > maxval:
                maxval = current.value
            current = current.next
        return maxval

node = ListNode(1)
dll = DoublyLinkedList(node)
dll.delete(node)
dll.add_to_tail(1)
dll.add_to_head(9)
dll.add_to_tail(6)
dll.delete(dll.head)
current = dll.head
while current:
    print(current.value)
    current = current.next
