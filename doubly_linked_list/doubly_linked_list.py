"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
from math import inf


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
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # remember old head value
        old_head = self.head
        # create new head node
        self.head = ListNode(value, next=old_head)
        # set .prev pointer of old head to new head
        if old_head:
            old_head.prev = self.head
        # increment length
        self.length += 1
        if self.length == 1:
            # if the node is added to an empty dll it is both the head and tail
            self.tail = self.head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        removed = self.head
        self.head = removed.next
        self.length -= 1
        if not self.head:
            self.tail = None
        return removed.value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        old_tail = self.tail
        self.tail = ListNode(value, old_tail)
        if old_tail:
            old_tail.next = self.tail
        self.length += 1
        if self.length == 1:
            self.head = self.tail

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            return None

        old_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.prev
            self.tail.next = None
        self.length -= 1
        return old_tail.value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        old_head = self.head
        self.head = node
        self.head.next = old_head
        self.head.prev = None

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        old_tail = self.tail
        self.tail = node
        self.tail.next = None
        # must update head for lists of 2
        if node is self.head and self.length == 2:
            self.head = old_tail
            self.head.next = self.tail
        if old_tail:
            self.tail.prev = old_tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if node is self.head:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif node is self.tail:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.length == 0:
            return None

        largest = -inf
        current = self.head
        try:
            while current:
                if current.value > largest:
                    largest = current.value
                current = current.next

        except:
            return largest
        return largest
