"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
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
        # wrap the value in a new Node
        new_node = ListNode(value)
        # increment the length
        self.length += 1
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the Last node's "next_node" to the new node
            new_node.next = self.head
            # set the current head's 'prev' to refer to the new_node
            self.head.prev = new_node
            # update the "self.tail" to point to the new node that we just added
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.

    * need to review
    """
    def remove_from_head(self):
        # if self.head is None and self.tail is None:
        #     return None
        # elif self.head is self.tail:
        #     value = self.head.value
        #     self.head = None
        #     self.tail = None
        #     return value
        # else:
        value = self.head.value
        self.delete(self.head)
        return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = ListNode(value)
        # increment the length
        self.length += 1
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the Last node's "next_node" to the new node
            new_node.prev = self.tail
            # set the current head's 'prev' to refer to the new_node
            self.tail.next = new_node
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if self.head is None and self.tail is None:
        #     return None
        # elif self.head is self.tail:
        #     value = self.head.value
        #     self.head = None
        #     self.tail = None
        #     return value
        # else:
        value = self.tail.value
        self.delete(self.tail)
        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)
        pass

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
        # update head, tail
        # Empty list
        if self.head is None:
            return None
        # Only 1 node
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head: # list has +2 nodes
            self.head = node.next
            node.delete() # updating prev and/or next pointeres
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        # update length
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        curr_node = self.head
        while curr_node:
            if curr_node.value > max_value:
                max_value = curr_node.value

            curr_node = curr_node.next
        return max_value



"""
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
"""

#-------------------------------------------------------------------------
