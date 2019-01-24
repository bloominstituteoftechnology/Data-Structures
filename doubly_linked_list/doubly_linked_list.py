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
        if self.head is None:
            self.head = ListNode(value)
        else:  # We have at least a head and a tail
            old_head = self.head
            self.head = ListNode(value)
            old_head.prev = self.head
            self.head.next = old_head

    def remove_from_head(self):
        prev_head = self.head
        prev_head.next.prev = None
        self.head = self.head.next
        return prev_head.value

    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail)
        self.tail.next = new_node
        self.tail = new_node

    def remove_from_tail(self):
        prev_tail = self.tail
        prev_tail.prev.next = None
        self.tail = prev_tail.prev
        return prev_tail.value

    def move_to_front(self, node):
        old_head = self.head
        old_head.prev = node
        self.head = node
        self.head.next = old_head
        node.delete

    def move_to_end(self, node):
        old_tail = self.tail
        old_tail.next = node
        self.tail = node
        self.tail.prev = old_tail

    def delete(self, node):
        node.delete()

    def get_max(self):
        if self.head is None:
            return None

        max_value = self.head
        curr_node = self.head

        while True:
            if curr_node is None:
                return max_value.value
            elif curr_node.value > max_value.value:
                max_value = curr_node

                curr_node = curr_node.next
