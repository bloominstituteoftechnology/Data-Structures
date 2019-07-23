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
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, prev=None, next=None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def remove_from_head(self):
        if not self.head:
            return None
        self.length -= 1

        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return current_head

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_from_tail(self):
        if not self.tail:
            return None

        self.length -= 1

        if self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            return current_tail.value
        else:
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        return current_tail

    def move_to_front(self, node):
        if node == self.head:
            return

        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(node.value)

    def move_to_end(self, node):
        if node == self.tail:
            return

        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(node.value)

    def delete(self, node):

        if self.head is self.tail:
            self.remove_from_head()

        elif self.head is node:
            self.remove_from_head()

        elif self.tail is node:
            self.remove_from_tail()

    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value
