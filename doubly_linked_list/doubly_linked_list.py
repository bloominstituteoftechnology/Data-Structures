"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

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

    def add_to_head(self, value):
        # if there head is None
        if self.head is None:
            # Add a head
            self.head = ListNode(value, None, value)
            # Add a tail
            self.tail = ListNode(value, value, None)
        else:
            # store current head in next value
            next_val = self.head
            self.head = ListNode(value, None, next_val)

    def remove_from_head(self):
        # store old head in variable
        if self.head:
            # store old head in temp variable
            removed = self.head.value
            # update head to next value
            self.head = self.head.next
            return removed

    def add_to_tail(self, value):
        # if there is a current tail
        if self.tail is not None:
            # store old tail in temp variable
            prev_tail = self.tail
            # update tail to next value
            self.tail = ListNode(value, prev_tail, None)

    def remove_from_tail(self):
        if self.tail:
            removed = self.tail.value
            self.tail = self.tail.prev
            return removed

    def move_to_front(self, node):
        prev_front = self.head
        self.head = ListNode(node, None, prev_front)
        # self.tail = ListNode(prev_front, self.head, None)

    def move_to_end(self, node):
        pass

    def delete(self, node):
        return node.delete()

    def get_max(self):
        pass
