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
          # get a ref to the current head [0]
        current_head = self.head
        # if it is none, make a new head from passed value
        if not current_head:
            self.head = ListNode(value)
        else:
              # if it is not the head, add it before and turn the previous head into the previous value
            current_head.insert_before(value)
            self.head = current_head.prev

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            head = self.head
            self.head.delete()
            return head.value

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.insert_after(new_node)
            self.tail = new_node

    def remove_from_tail(self):
        # if no tail return none
        if not self.tail:
            return None
            # if tail is also the head, make both == None
        if not self.tail.prev:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.value
            # if tail is not also the head, remove it
        else:
            tail = self.tail
            self.tail.delete()
            self.tail = self.tail.prev
            return tail.value

    def move_to_front(self, node):
        # check if already is in front
        if self.head is not node:
            if node.next and node.prev:  # if in a middle spot
                node.prev.next = node.next
                node.next.prev = node.prev
            current_head = self.head
            self.head = node
            node.next = current_head
            current_head.prev = node

    def move_to_end(self, node):
            # check if the nodelist is empty
        if not self.head:
            return None
        current_node = self.tail
        while current_node:
            if current_node.value == node:
                return self.add_to_tail(node)
            current_node = current_node.prev

    def delete(self, node):
        pass

    def get_max(self):
        pass
