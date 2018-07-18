# Each ListNode holds a reference to its previous node as well as its next node in the list
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # wrap the given value in a ListNode and insert it after this node
    # Note that this Node could already have a next node it is pointing to
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next:
            current_next.prev = self.next

    # Wrap the given value in a ListNode and insert it before this node
    # Note that this Node could already have a previous node it is point to
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)

        if current_prev:
            current_prev.next = self.prev

    # Rearranges this ListNode's previous and next pointers
    # accordingly, effictively deleting this ListNode
    def delete(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev


# Our doubly-linked list class. It holds references to the list's head and tail nodes
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    # Wraps the given value in a ListNode and inserts it as the new head of the list
    # Don't forget to handle the old head node's previous pointer accordingly
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node

    # Removes the List's current head node, making the current head's next node the new head of the List.
    # Returns the removed node
    def remove_from_head(self):
        if not self.head:
            if not self.tail:
                return None
            return self.remove_from_tail()
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return current_head.value

    # Wraps the given value in a ListNode and inserts it as the new tail of the list
    # Don't forget to handle the old tail node's next pointer accordingly
    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value, self.head, None)
        elif not self.head:
            self.head = self.tail
            self.tail = ListNode(value, self.head, None)
            self.head.next = self.tail
        else:
            self.tail = ListNode(value, self.head, None)
            self.tail.prev.next = self.tail

    # Removes the List's current tail node, making the current tail's previous node the new tail of the List
    # # Returns the removed Node
    def remove_from_tail(self):
        if not self.tail:
            if not self.head:
                return None
            return self.remove_from_head()
        else:
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return current_tail.value

    # Removes the input node from its current spot in the List and inserts it as the new head node of the List
    def move_to_front(self, node):
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(value)

    # Removes the input node from its current spot in the List and inserts it as the new tail node of the List
    def move_to_end(self, node):
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
        self.add_to_tail(value)

    def delete(self, node):
        node.delete()
