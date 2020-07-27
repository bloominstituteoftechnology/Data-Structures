"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        else:
            new_node = ListNode(value, next=self.head)
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            value = self.head.value
            self.delete(self.head)
            return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if not self.tail:
            self.head = ListNode(value)
            self.tail = self.head
            self.length += 1
        else:
            new_node = ListNode(value, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            return None
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            # already at the front do nothing
            return
        else:
            self.delete(node)

        # glue it at the front
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        # to offset the deletion
        self.length += 1

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            self.delete(node)

        # glue it at the end
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        # to account for the node delition
        self.length += 1

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # Check if the only node
        if (node is self.head) and (node is self.tail):
            self.head = None
            self.tail = None
            self.length -= 1

        # Check if head with other nodes
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

        # Check if tail with other nodes
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1

        # All Else
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        else:
            current = self.head
            largest = self.head

            while current:
                if current.value > largest.value:
                    largest = current

                current = current.next

            return largest.value
