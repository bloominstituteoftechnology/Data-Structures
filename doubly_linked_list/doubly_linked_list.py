"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        """Rearranges previous and next pointers"""
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
        
        # turn value into an object of ListNode
        new_node = ListNode(value)
        # increase length by 1
        self.length += 1

        # check to see if there is already a head (if DLL is empty)
        # doesn't account for a weird case in which there would be a
        # head but no tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        
        current_head = self.head
    
        if not current_head:
            return None
        self.delete(self.head)
        return current_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        
        new_node = ListNode(value)
        self.length += 1

        # DLL empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node    
        # DLL not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        
        current_tail = self.tail

        # DLL empty
        if not self.head:
            return None
        # DLL not empty
        self.delete(self.tail)        
        return current_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # look to see if node is at the beginning already
        if not node.prev:
            return "Already in front"
        # if node is the tail
        elif not node.next:
            # set previous.next to None
            node.prev.next = None
            # set previous node to tail
            self.tail = node.prev
            # set node's next to current head
            node.next = self.head
            # set node's prev to None
            node.prev = None
            # set current head's node's prev to node
            self.head.prev = node
            # point head to node
            self.head = node
        else:
            # set node's prev next to node's next
            # set node's next prev node's prev
            node.prev.next, node.next.prev = node.next, node.prev
            
            # set the current head's prev to new node
            self.head.prev = node
            # set node's next to the current head
            node.next = self.head
            # set node's prev to None
            node.prev = None
            # set head to node
            self.head = node
            
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # look to see if it is already at the end already
        if not node.next:
            # if it is, return "at end"
            return ("already at the end")
        # look to see if it is at the beginning
        elif not node.prev:
            # if it is
            # set node.next.prev = None
            node.next.prev = None
            # assign head to node.next
            self.head = node.next
            # assign tail.next to node
            self.tail.next = node
            # assign node.prev to tail
            node.prev = self.tail
            # assign tail to node
            self.tail = node
        else:
            # set node's prev next to node's next
            # set node's next prev node's prev
            node.prev.next, node.next.prev = node.next, node.prev
            # set node's prev to current tail
            node.prev = self.tail
            # set current tail's next to node
            self.tail.next = node
            # set node's next to None
            node.next = None
            # set tail to node
            self.tail = node
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        # if no other item in list:
        if (not node.next) and (not node.prev):
            # set tail to None
            self.tail = None
            # set head to None
            self.head = None
        # check to see if it's at the beginning
        elif not node.prev:
            # change node.next.prev = None
            node.next.prev = None
            # set head to node.next
            self.head = node.next
        # check to see if it's at the end
        elif not node.next:
            # change node.prev.next = None
            node.prev.next = None
            # set tail to node.prev
            self.tail = node.prev
        else: 
            # set node's prev next to node's next
            # set node's next prev node's prev
            node.prev.next, node.next.prev = node.next, node.prev

        # TODO:
            # if self.prev:
            #     self.prev.next = self.next
            # if self.next:
            #     self.next.prev = self.prev


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # check to see if empty
        if not self.head:
            return None
        # create reference to largest value we've seen
        max_value = self.head.value
        # reference to current node as we traverse
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # compare current value to max value
            if current.value > max_value:
                # assign max to current
                max_value = current.value
            # iterate through current
            current = current.next
            # return max
            
        return max_value
