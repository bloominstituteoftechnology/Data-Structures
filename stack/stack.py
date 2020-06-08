"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:  # Node class
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
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Wrap given value in a ListNode
        new_node = ListNode(value)
        # Increase the lenght by 1
        self.length += 1
        # Handle if list has a head
        if self.head:
            # set the next node to the crruent head
            new_node.next = self.head
            # chnage the  previous current head to node
            self.head.prev = new_node
            # instert the new node at head
            self.head = new_node

        # Handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):  # TODO: Ask TL about this tomorrow
        # Declare value
        value = self.head.value
        # Delete head node
        self.delete(self.head)
        # Return the value of the removed node
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # Wrap given value in a ListNode
        new_node = ListNode(value)
        # Increase the lenght by 1
        self.length += 1
        # Handle if list has a tail
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        # Handle if list has no tail
        else:
            self.tail = new_node
            self.head = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):  # TODO: Ask TL about this tomorrow
        # Declare value
        value = self.tail.value
        # Delete tail node
        self.delete(self.tail)
        # Return the value of the removed node
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # If list is empty
        if not self.head:
            print("Nothing here today!")
            return

        self.length -= 1

        # If list has one item
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # If two nodes are in the list, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None

        # If two nodes are in the list, and the node we want to delete is the head
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.delete()  # TODO: "Do further research to get a better understanding of this line of code"

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


""" DLL Storage Structure
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_from_head()

    def __len__(self):
        return self.storage.length
"""

# Array Structure


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = [1, 2, 3]

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    # def __len__(self):
    #    return self.storage.length
