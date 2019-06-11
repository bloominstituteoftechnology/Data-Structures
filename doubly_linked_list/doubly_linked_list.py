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
        new_node = ListNode(value)
        if self.head is not None:
            previous_head = self.head
            self.head = new_node
            self.head.next = previous_head
            previous_head.prev = self.head
            self.length += 1
            return self.head.value

        else:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            self.length += 1
            return self.head.value

    def remove_from_head(self):
        if self.head is not None:
            deleted_head_value = self.head.value
            self.head.delete()
            self.length -= 1
            return deleted_head_value
        else:
            return None

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is not None:
            previous_tail = self.tail
            self.tail = new_node
            self.tail.prev = previous_tail
            previous_tail.next = self.tail
            return self.tail.value

        else:
            self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return self.tail.value

    def remove_from_tail(self):
        if not self.tail:
            return None
        self.tail.delete()
        self.tail = None
        self.length = self.length - 1

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        self.delete(self)
        self.length = self.length - 1

    def get_max(self):
        return len(self)
