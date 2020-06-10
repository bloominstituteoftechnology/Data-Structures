"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
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
        new_node = ListNode(value, None, self.head)
        # the new node will be both the new head and also the tail if the list was empty
        if self.length == 0:
            self.tail = new_node
        else:
            # make new node the prev of the old head
            self.head.prev = new_node
        self.length += 1
        self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length > 0:
            old_head = self.head
            self.head = self.head.next # set a new head
            self.length -= 1
            if self.length == 1:
                # If there is not another node in the list, make the new head's prev value None to remove the pointer to the old head. This will make the Python runtime delete the old head as well.
                self.head.prev = None
            else:
                # If the list is now empty then the head should be None (already done above) and tail should also be none.
                self.tail = None
            return old_head.value
        else:
            print("You cannot remove a node because the list is already empty.")    
            

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, self.tail, None)
        if self.length > 0:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length > 0:
            old_tail = self.tail
            self.tail = self.tail.prev
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.next = None
            self.length -= 1
            return old_tail.value
        else:
            print("You cannot remove a node because the list is already empty.")

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node == self.head:
            return
        else:    
            self.head.prev = node # do this first so that we don't lose the reference
            if node == self.tail:
                # set new tail if moving tail
                node.prev.next = None
                self.tail = node.prev
            else:
                # connect the nodes before and after the moved node if it's a middle node
                node.prev.next = node.next
                node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            self.tail.next = node
            if node == self.head:
                node.next.prev == None
                self.head = node.next
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            
        node.prev = self.tail
        node.next = None
        self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node == self.head:
            # set new head
            if self.head.next: # if there is more than one node
                # self.head.next.prev = None ----- is done by delete method
                self.head = self.head.next
            else:
                self.head = None
        if node == self.tail:
            # set new tail
            if self.tail.prev:
                # self.tail.prev.next = None ----- is done by delete method
                self.tail = self.tail.prev
            else:
                self.tail = None
        node.delete()
        self.length -= 1

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head == None:
            return None
        max_so_far = self.head.value
        current = self.head.next
        while current != None:
            if current.value > max_so_far:
                max_so_far = current.value
            current = current.next

        return max_so_far
