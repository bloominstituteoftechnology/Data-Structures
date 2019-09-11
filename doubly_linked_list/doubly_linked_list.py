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

    def add_to_head(self, value):  # PASS
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        return_value = self.head.value
        self.delete(self.head)
        return return_value

    def add_to_tail(self, value):
        # wrap value in a node
        new_tail = ListNode(value)
        self.length += 1
        # update the old tail's next reference to refer to the new node
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

            new_tail.next = None

    def remove_from_tail(self):
        return_value = self.tail.value
        self.delete(self.tail)
        return return_value

    def move_to_front(self, node):  # error
        if node is self.head:
            return
        elif node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node)
            # make it the new head
        self.add_to_head(node.value)

    def move_to_end(self, node):  # similar to move to front #FAIL
        if node is self.tail:
            return
        elif node is self.head:
            self.remove_from_head()
        else:
            self.delete(node)

        self.add_to_tail(node.value)

    def delete(self, node):  # FAIL
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):  # ERROR
        if self.head is None:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
