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
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    def move_to_front(self, node):
        if node is self.head:
            return
        node_value = node.value
        self.delete(node)
        self.add_to_head(node_value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        node_value = node.value
        self.delete(node)
        self.add_to_tail(node_value)

    def delete(self, node):
        self.length -= 1
        if self.head is None and self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            node.delete()
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        if self.head is None:
            return None
        max_val = self.head.value
        curr_val = self.head
        while curr_val:
            if curr_val.value > max_val:
                max_val = curr_val.value
            curr_val = curr_val.next
        return max_val
