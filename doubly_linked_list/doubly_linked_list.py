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
        new_node = ListNode(value) # Wraps the given value in a ListNode
        if not self.head: # if empty set the head and tail to the new_node
            self.head = new_node
            self.tail = new_node
            self.length += 1 # length has increased by 1
        else:
            self.head = new_node # state that the new node will be the head
            new_node.prev = None # state that the new node prev is None (nothing before the head)
            new_node.next = self.head # state that the new node next will be the current head
            self.head = new_node # now that you've stated all that above, time travel forward, and behold the current head is now the new node!
            self.length += 1 # increase the length by 1, because you have a new node as the head!

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head: # if empty set the head to None
            self.head = None
        else:
            new_leader = self.head.next # state that the next in line for the throne will take over eventually
            new_leader.prev = None # state that the new leader will not have anybody ruling above them
            self.length -= 1 # coup

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail: # check to see if empty DLL
            self.head = new_node # set the head and tail to the new node because it's empty
            self.tail = new_node
        else: # otherwise if it's not empty
            new_node.prev = self.tail # make the new node point (prev) to the original tail
            self.tail.next = new_node # make the original tail point (next) to the new node
            self.tail = new_node # make the new node the new tail

        # new_node = ListNode(value) # Wraps the given value in a ListNode
        # if not self.head: # if empty set the head and tail to the new_node
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     current_node = self.head # declare a starting point
        #     while current_node.next is not None: # loop
        #         current_node = current_node.next # keep going through the nodes as long as next != None
        #     current_node.next = new_node # if next == None, that means this is the tail, so set the next pointer to the new_node
        #     new_node.insert_after = None # insert a node after this one, label it as None
        #     self.tail = new_node # because the tail is now the new_node
        #     self.length += 1 # since we inserted the new_node as the tail, increase by 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail) # delete tail from DLL
        return value

        # if not self.tail: 
        #     if not self.head: 
        #         return None 
        # else: 
        #     original_tail = self.tail # declare this as the starting tail
        #     new_tail = original_tail.prev # set the new tail as the prev
        #     new_tail.next = None # set the new tail as the tail
        #     self.length -= 1 # we got rid of a node, decrease by 1
        #     return original_tail # returns the value of the removed Node

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        wanna_be_line_leader_node = node.delete
        leader_node = self.head
        leader_node.add_to_head(wanna_be_line_leader_node)
        # don't need to edit length because we are deleting -1 and adding +1

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        wanna_be_caboose_node = node.delete
        caboose_node = self.tail
        caboose_node.add_to_tail(wanna_be_caboose_node)
        # don't need to edit length because we are deleting -1 and adding +1

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail: # check to see if empty
            return # if empty, there is nothing to delete, so return
        self.length -= 1 # when deleting, decrease by 1
        if self.head == self.tail: # if DLL has 1 element, remove it
            self.head = None # by setting head and tail to None
            self.tail = None
        elif self.head == node: # if node is the head
            self.head = node.next # set DLL head pointer to next
            node.delete() # remove node connections 
        elif self.tail == node: # if node is the tail
            self.tail = node.prev # set DLL tail pointer to prev
            node.delete() # remove node connections
        else: # more than 3 nodes, not head or tail
            node.delete()

        # current_node = self.head
        # if node == self.head: # check to see if the node was the head
        #     self.remove_from_head # if so, remove
        #     self.length -= 1 # decrease length
        # elif node == self.tail: # check to see if the node was the tail
        #     self.remove_from_tail # if so, remove
        #     self.length -= 1 # decrease length
        # else:
        #     while current_node is not None: # loop over until you reach the tail
        #         current_node = current_node.next # see the current node to the next one
        #         if current_node.value == node.value: # if current node is the node you want to delete
        #             current_node.prev = current_node # set the prev to current node
        #             current_node = current_node.next # and current node to next 
        #     current_node = None # (so it overlaps, therefore deleting it)
        #     self.length -= 1 # decrease length

    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head # declare a starting point
        while current_node.next is not None: # loop
            current_node = current_node.next # keep going through the nodes as long as next != None
        return current_node.value # should be the max? because it's the last node's value (tail)