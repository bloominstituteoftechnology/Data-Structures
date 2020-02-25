"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
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
    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
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
        # new_node = ListNode(key, value)
        self.length += 1
        if not self.head and not self.tail:
            # empty list, head and tail
            self.head = self.tail = ListNode(key, value)
        else:
            self.head.insert_before(key, value)
            self.head = self.head.prev


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # empty list, head and tail
            self.head = self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):

         # if LL is empty
        if not self.head and not self.tail:
            print("Error: attempted to delete node not in list")
            return
         # if node is both head and tail
        elif self.head == self.tail:
            self.head = None
            self.tail = None
         # if node is head
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        # if node is tail
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        # if node is in the middle
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value
        iterator = self.head

        while iterator is not None:
            if iterator.value > max_value:
                max_value = iterator.value
            iterator = iterator.next
        
        return max_value

