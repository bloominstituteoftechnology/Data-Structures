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
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

        else:
            self.head, self.tail = new_node, new_node
            self.length += 1

    def remove_from_head(self):
        if self.head is not None:
            self.head.delete()
            self.length -= 1
        else:
            self.head = None
            self.length = 0

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.tail is not None:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1

        else:
            self.head, self.tail = new_node, new_node
            self.length += 1

    def remove_from_tail(self):
        if self.tail is not None:
            future_tail = self.tail.prev
            self.tail.delete()
            self.length -= 1
            self.tail = future_tail
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def move_to_front(self, node):
        if node == self.tail:
            self.tail = self.tail.prev

        previous_head = self.head
        self.head = node
        self.head.next = previous_head
        previous_head.prev = self.head

    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next

        previous_tail = self.tail
        self.tail = node
        self.tail.prev = previous_tail
        previous_tail.next = self.tail

    def delete(self, node):
        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        self.length -= 1
        node.delete()

    def get_max(self):
        if self.head is not None:
            curr_node = self.head.next
            max_value = self.head
            while curr_node:

                if curr_node.value > max_value.value:
                    max_value = curr_node
                curr_node = curr_node.next
            return max_value.value
        else:
            return None
