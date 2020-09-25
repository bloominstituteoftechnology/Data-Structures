"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next = next_node

    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next


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
        # create new_node
        new_node = ListNode(value)
        # 1. add to empty
        # update head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 2. add to none empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            val = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return val

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # empty list
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Set new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            val = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        else:
            val = self.tail.value
            self.tail.prev.next = None
            self.tail.prev = self.tail
            self.length -= 1
            return val

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node is self.head:
            return
        # 1. delete
        self.delete(node)
        # 2. add_to_head()
        self.add_to_head(node.value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node is self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # don't need to return value

        # need to update head and tail
        if self.head is None:
            return
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:  # list has to have atleast 2+ nodes
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            return self.head.value
        else:
            high = -float('Inf')
            current = self.head
            while current:
                if high < current.value:
                    high = current.value
                    current = current.next
                else:
                    current = current.next
        return high
