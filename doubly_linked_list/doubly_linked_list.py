"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, key, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.key = key

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

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, key, value):
        print(key)
        new_node = ListNode(key, value, None, None)
        self.length += 1
        # base case - empty list
        if not self.head and not self.tail:
            self.head = self.tail = new_node
        # will execute adding the node to the head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly."""

    def add_to_tail(self, key, value):
        new_node = ListNode(key, value, None, None)
        self.length += 1
        # base case - empty list
        if not self.head and not self.tail:
            self.head = self.tail = new_node
        # will execute adding the node to the head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return None
        key = self.head.key
        value = self.head.value
        self.delete(self.head)
        return value, key

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        key = self.tail.key
        value = self.tail.value
        self.delete(self.tail)
        return value, key

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        key = node.key
        value = node.value
        self.delete(node)
        self.add_to_head(key, value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        key = node.key
        value = node.value
        self.delete(node)
        self.add_to_tail(key, value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
            return

        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()

        else:
            node.delete()
        self.length -= 1



    """Returns the highest value currently in the list"""
    def get_max(self):
        current_value = self.head
        max_value = current_value.value
        while current_value is not None:
            if current_value.value > max_value:
                max_value = current_value.value
            current_value = current_value.next
        return max_value











    # def single_list(single_link_list):
    #     current_node = single_link_list.head
    #     previous_node = None
    #     counter = 0
    #
    #     while True:
    #         previous_node = current_node
    #         current_node = current_node.next
    #         if current_node.next == None:
    #             break
    #         if counter == 0:
    #             previous_node.next = None
    #         current_node.next = previous_node
    #         counter += 1
    #
    #
    #     return single_link_list




