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
        # Create new node
        new_node = ListNode(value)
        # If no head then set new node as head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # set new_node next to current head
            new_node.next = self.head
            # set curr head prev to new head
            self.head.prev = new_node
            # set new_node as head
            self.head = new_node

    def remove_from_head(self):
        # Initially define old head as None
        old_head = None
        # If head is defined
        if self.head is not None:
            # set old head before changing to new head
            old_head = self.head
            # delete old head from link list
            del(self.head)
            # set new head from old head next
            self.head = old_head.next
            # Set new head prev to None
            self.head.prev = None

        # return old head
        return old_head.value

    def add_to_tail(self, value):
        # define new node with prev as old tail
        new_node = ListNode(value, prev=self.tail)
        # define next on old tail
        self.tail.next = new_node
        # define tail as new node
        self.tail = new_node

    def remove_from_tail(self):
        # Initially define old tail as None
        old_tail = None
        # If tail is defined
        if self.tail is not None:
            # set old tail before changing to new tail
            old_tail = self.tail
            # Delete old tail from linked list
            del(self.tail)
            # set new tail from old tail prev
            self.tail = old_tail.prev
            # set new tail next to None
            self.tail.next = None
        return old_tail.value

    def move_to_front(self, node):
        node.delete()
        self.add_to_head(node.value)

    def move_to_end(self, node):
        node.delete()
        self.add_to_tail(node.value)

    def delete(self, node):
        if node.next is None:
            node.prev.next = None
        elif node.prev is None:
            node.next.prev = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

    def get_max(self):
        max_val = float("-inf")
        curr_node = self.head
        while True:
            if curr_node is None:
                return None

            if curr_node.value > max_val:
                max_val = curr_node.value

            if curr_node.next == None:
                return max_val
            else:
                curr_node = curr_node.next
