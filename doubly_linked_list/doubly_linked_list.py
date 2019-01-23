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
        # create a new node
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # set the tail of new node to old head
            new_node.next = self.head
            # set head to a new node
            self.head = new_node

    def remove_from_head(self):
        # check if the head is None
        if self.head:
            # set the head node's next node value to a temp var
            old_head = self.head
            # del the head node
            del self.head
            # then set head to that temp
            self.head = old_head.next

            if self.head is None:
                self.tail = None

            return old_head.value

    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # set the head of new node to old tail
            new_node.prev = self.tail
            # set tail to a new node
            self.tail = new_node

    def remove_from_tail(self):
        # check if the head is None
        if self.tail:
            # set the head node's next node value to a temp var
            old_tail = self.tail
            # del the head node
            del self.tail
            # then set head to that temp
            self.tail = old_tail.prev

            if self.tail is None:
                self.head = None

            return old_tail.value

    def move_to_front(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def delete(self, node):
        node.delete()

    def get_max(self):
        if self.head:
            # set initial max value to head
            current = self.head
            max_value = current.value

            while current:  # while current is not None
                if max_value < current.value:
                    max_value = current.value

                # keep going to the next node
                current = current.next

            return max_value
        else:
            return None


dll = DoublyLinkedList()
dll.add_to_head(1)
print(dll.get_max())
