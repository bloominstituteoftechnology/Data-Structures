"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

# These are methods for the node
class ListNode:
    def __init__(self, value, prev=None, next=None):
        # These three functions are all that is needed to implement a linked list.
        # https://youtu.be/0y8RGU1-KqI?t=3398
        self.value = value   # Retreve the value in the current node
        self.prev = prev    # Retrieve the pointer of the previous node
        self.next = next   # Retrieve the pointer to the next node in the list.

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

# These are methods for the linked list
# https://youtu.be/0y8RGU1-KqI?t=3524
class DoublyLinkedList:
    def __init__(self, node=None):  # This is useful but not required to create a linked list.
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0 # Initialize this list to have the one

    def __len__(self):
        return self.length # This returns the length of the list.  It allows calling the built in len() function on the list.

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
    # https://youtu.be/0y8RGU1-KqI?t=3694
    # Create a double linked list

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if it is already the head just return
        # if it is not grab the value in that node
        # delete the node
        # add the node value to the head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if it is already the tail just return
        # if it is not grab the value in that node
        # delete the node
        # add the node value to the tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # This delete removes a node from the list.
        # https://youtu.be/0y8RGU1-KqI?t=3607 
        # TODO: Catch errors if list is empty or node is not in list
        # First pass we are assuming node is in the list
        self.length -= 1 #Adjust the length of the list
        # if node is head and tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # We must loop through the entire list to find the biggest value: O(n)
        # TODO: Error checking
        # If there is no list return
        # Get the value of the head = max value to start
        # Use a while loop to iterate
        # Get the value and text
        # When the tail is reached the current becomes nil and ends the while list
        # Return the max value

