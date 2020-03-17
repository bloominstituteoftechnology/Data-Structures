"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    # """Wrap the given value in a ListNode and insert it
    # after this node. Note that this node could already
    # have a next node it is point to."""
    # def insert_after(self, value):
    #     current_next = self.next
    #     self.next = ListNode(value, self, current_next)
    #     if current_next:
    #         current_next.prev = self.next

    # """Wrap the given value in a ListNode and insert it
    # before this node. Note that this node could already
    # have a previous node it is point to."""
    # def insert_before(self, value):
    #     current_prev = self.prev
    #     self.prev = ListNode(value, current_prev, self)
    #     if current_prev:
    #         current_prev.next = self.prev

    # """Rearranges this ListNode's previous and next pointers
    # accordingly, effectively deleting this ListNode."""
    # def delete(self):
    #     if self.prev:
    #         self.prev.next = self.next
    #     if self.next:
    #         self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return 'empty'
        curr_node = self.head
        output = ''
        output += f'({curr_node.value }) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'({curr_node.value }) <-> '
        return output
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding new value to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list only has one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            # this will become the new head
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # adding to the end of a list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list only has one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            # this will become the new head
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        node_value = node.value
        self.delete(node)
        self.add_to_head(node_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        node_value = node.value
        self.delete(node)
        self.add_to_tail(node_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

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

    """Returns the highest value currently in the list"""

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


# our_dll = DoublyLinkedList()
# our_dll.add_to_head(5)
# our_dll.add_to_head(3)
# our_dll.add_to_tail(10)
# our_dll.add_to_tail(1)
# our_dll.add_to_head(12)
# removed_val = our_dll.remove_from_head()
# second_removed_val = our_dll.remove_from_tail()
# print(our_dll)
# print(removed_val)
# print(second_removed_val)
