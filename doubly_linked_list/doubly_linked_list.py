class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly."""
        if self.head is None:
            self.head = ListNode(value)
            self.tail = self.head
            return
        self.head.insert_before(value)
        self.head = self.head.prev
        if self.tail is None:
            self.tail = self.head

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""
        if self.head is None:
            return None
        new_head, old_head_value = self.head.next, self.head.value
        self.head.delete()
        self.head = new_head
        if self.head is None:
            self.tail = None
        return old_head_value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next pointer accordingly."""
        if self.tail is None:
            self.tail = ListNode(value)
            self.head = self.tail
            return
        self.tail.insert_after(value)
        self.tail = self.tail.next
        if self.head is None:
            self.head = self.tail

    def remove_from_tail(self):
        """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
        if self.tail is None:
            return None
        old_tail_value, new_tail = self.tail.value, self.tail.prev
        self.tail.delete()
        self.tail = new_tail
        if self.tail is None:
            self.head = None
        return old_tail_value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new head node of the List."""
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List."""
        self.delete(node)
        self.add_to_tail(node.value)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""
        if node is None:
            return
        if self.tail == node:
            self.remove_from_tail()
        if self.head == node:
            self.remove_from_head()
        else:
            node.delete()

    def get_max(self):
        """Returns the highest value currently in the list"""
        if self.head is None:
            return None
        current = self.head
        current_max = current.value
        while current.next is not None:
            current_max = max(current_max, current.next.value)
            current = current.next
        return current_max

    def contains(self, node):
        """Returns True if node is in list, False if not"""
        current = self.head
        while current is not None:
            if current == node:
                return True
        return False
