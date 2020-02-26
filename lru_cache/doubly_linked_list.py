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
        """ add_to_head, define a new node. check"""
        new_node = ListNode(value, None, None)
        self.length += 1
        if self.head is not None and self.tail is not None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        pass

    def remove_from_head(self):
        value = self.head.value # grab the value at the head
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):

        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
        pass

    def delete(self, node):
        # let's define the base cases
        # obviously, delete is going to lower the length of the list
        self.length -=1

        # think of special cases
        if not self.head and not self.tail:
            return

        # if head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # if head
        if self.head == node:
            self.head = self.head.next      # change the pointer of the head
            node.delete()

        if self.tail == node:
            self.tail = self.tail.next
            node.delete()

        else:
            node.delete()


    def get_max(self):
        if not self.head:
            return None

        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
