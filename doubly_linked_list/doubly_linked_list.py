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
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # first, let's get the new_node connected as the current head's prev
            self.head.prev = new_node
            # then, get that new_node's next connector latched onto the current head
            self.head.prev.next = self.head
            # then, you change the head to the new_node
            self.head = new_node
            # increment length
            self.length += 1

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        old_head_value = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        
        else: 
            self.head = self.head.next
            self.head.prev = None
            # lol, what even happens to the old head? i think its just floating there
            return old_head_value

    def add_to_tail(self, value):
        pass

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
