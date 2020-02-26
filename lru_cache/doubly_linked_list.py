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
    def add_to_head(self, value): #  node is a part of linked list, list in entire thing
         
        new_node = ListNode(value, None, None) # create node

        # Scenarios we need to think about:
        # This needs to be head because we're adding to head
        # Update previous head
        # Increase length
        
        # Edge cases? -- If self.head is none, then there is no list and no tail
        # If there is no tail... new becomes new tail as well

        self.length += 1 # if empty add something 
        if not self.head and not self.tail: # If there is no list(empty), this is head and tail...
            self.head = new_node # new head
            self.tail = new_node # new tail
        else: # We now know the list is populated, so...
            new_node.next = self.head # make this node the head
            self.head.prev = new_node # rearrange the pointers
            self.head = new_node # this becoming new head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value # set current value to existing self.head.value
        self.delete(self.head) # delete self.head after setting value
        return value  # return new value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    # almost identical to add_to_head
    def add_to_tail(self, value): 

        new_node = ListNode(value, None, None) # create node

        self.length += 1 # if empty add something 
        if not self.head and not self.tail: # If there is no list(empty), this is head and tail...
            self.head = new_node # new head
            self.tail = new_node # new tail
        else: # We now know the list is populated, so...
            new_node.prev = self.tail # make this node the head
            self.tail.next = new_node # rearrange the pointers
            self.tail = new_node # this becoming new head

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value # set current value to existing self.tail.value
        self.delete(self.tail)  # delete self.tail after setting value
        return value # return new value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if node is self.head: #if head is moving...
        #     return  # we're done, we don't need to do anything
        # value = node.value    # else just set the value to node.value
        # if node is self.tail: # if tail is moving...
        #     self.remove_from_tail() # we have a function for this already
        # else:
        #     node.delete()           # otherwise, just delete the node
        # self.add_to_head(node)      # add the node to head using this function

        # A simpler way that uses what we've made more...
        value = node.value
        self.delete(node) 
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node): 
        self.length -= 1
    ##########
    # Scenarios we need to think about:
    # What if LL is empty?
    # What if node is head?
    # What if node is tail?
    # What if node is head and tail?
    # What if node is in the middle?
    ###########
        if not self.head and not self.tail:                         # If LL is empty
            print("Error: Attempted to delete node not in list")
            return
        elif self.head == self.tail:                                # If node is both head and tail (needs to be located here in elif chain because of Order of Operations)
            self.head = None                                            # head becomes None
            self.tail = None                                            # tail beccomes None
        elif node == self.head:                                     # If node is head
            self.head = self.head.next                                  # current head becomes the next
            node.delete()                                               # delete itself after setting self.head.next
        elif node == self.tail:                                     # If node is tail
            self.tail = self.tail.prev                                  # current tail becomes the previous
            node.delete()                                               # delete itself after setting self.tail.prev
        else:                                                       # If node is in middle
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None: 
            return None
        max_value = self.head.value # making maximum
        current = self.head         # making current
        while current:
            if current.value > max_value: # If node.value is higher
                max_value = current.value # update max
            current = current.next # loop to next
        return max_value # return max