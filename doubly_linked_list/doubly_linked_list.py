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
            node = ListNode(value)

            self.head = node
            self.tail = node

        else:
            self.head.insert_before(value)

            self.head = self.head.prev

    def remove_from_head(self):
        if self.head is None:
            return None

        else:
            prev_head = self.head.value

            if self.head.next is None:
                del(self.head)

                self.head = None
                self.tail = None

            else:
                new_head = self.head.next
                new_head.prev = None

                del(self.head)
                self.head = new_head

            return prev_head

    def add_to_tail(self, value):
        if self.tail is None:
            node = ListNode(value)

            self.head = node
            self.tail = node

        else:
            self.tail.insert_after(value)

            self.tail = self.tail.next

    def remove_from_tail(self):
        if self.tail is None:
            return None

        else:
            prev_tail = self.tail.value

            if self.tail.prev is None:
                del(self.tail)

                self.head = None
                self.tail = None

            else:
                new_tail = self.tail.prev
                new_tail.next = None

                del(self.tail)
                self.tail = new_tail

            return prev_tail

    def move_to_front(self, node):
        if self.head is node:
            pass

        else:
            if self.tail is node:
                self.tail = node.prev

            node.delete()

            node.prev, node.next = None, self.head
            self.head.prev = node

            self.head = node

    def move_to_end(self, node):
        if self.tail is node:
            pass

        else:
            if self.head is node:
                self.head = node.next

            node.delete()

            node.prev, node.next = self.tail, None
            self.tail.next = node

            self.tail = node

    def delete(self, node):
        if self.head is node:
            self.head = node.next

        if self.tail is node:
            self.tail = node.prev

        node.delete()

        del(node)

    def get_max(self):
        if self.head is None:
            return None

        curr_node = self.head
        max_node = -float("inf")

        while curr_node is not None:
            if curr_node.value > max_node:
                max_node = curr_node.value

            curr_node = curr_node.next

        return max_node
