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
        new_node = ListNode(value)
        if self.head is not None:
            # change self.head to the new node
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.prev = self.head
            return self.head.value
        else:
            self.head = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return self.head.value

    def remove_from_head(self):
        # check if head is none
        if self.head is not None:
            deleted_value = self.head.value
            self.head.delete()
            return deleted_value
        else:
            return None
            pass

    def add_to_tail(self, value):
        node = ListNode(value)
        # check if tail is none
        if self.tail is not None:
            prev_node = self.tail
            self.tail = node
            self.tail.prev = prev_node
            prev_node.next = self.tail
            return self.tail.value
        else:
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
            return self.tail.value
            pass

    def remove_from_tail(self):
        # check if tail is none
        if self.tail is not None:
            deleted_value = self.tail.value
            self.tail.delete()
            return deleted_value
        else:
            return None
            pass

    def move_to_front(self, node):
        old_head = self.head
        self.head = node
        self.head.next = old_head
        old_head.prev = self.head
        return self.head.value

        pass

    def move_to_end(self, node):
        old_tail = self.tail
        self.tail = node
        self.tail.prev = old_tail
        old_tail.next = self.tail
        return self.tail.value
        pass

    def delete(self, node):
        node.delete()
        pass

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
        pass
