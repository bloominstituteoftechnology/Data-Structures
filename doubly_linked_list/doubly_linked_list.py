from typing import Optional
from unittest.loader import defaultTestLoader

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev: Optional[ListNode] = prev
        self.next: Optional[ListNode] = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node that it is pointing to."""
    def insert_after(self, value):
        current_next = self.next
        node = ListNode(value, self, current_next)
        self.next = node
        if current_next:
            current_next.prev = self.next
        return node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node that it is pointing to."""
    def insert_before(self, value):
        current_prev = self.prev
        node = ListNode(value, current_prev, self)
        self.prev = node
        if current_prev:
            current_prev.next = self.prev
        return node

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
    def add_to_head(self, value):
        if self.head:
            self.head = self.head.insert_before(value)
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            removed_head = self.head
            self.delete(self.head)
            return removed_head.value
        else:
            return None
               
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail:
            self.tail = self.tail.insert_after(value)
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is not None:
            removed_tail = self.tail
            self.delete(self.tail)
            return removed_tail.value
        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node == self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.length -= 1
        node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max = None
        node = self.head

        while node:
            if not max:
                max = node.value
            elif node.value > max:
                max = node.value

            node = node.next
        
        return max
