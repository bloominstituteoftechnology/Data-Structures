"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next = next_node
            
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
        # Create instance of LN with value
        # Increment DLL length
        # Check if DLL empty 
        # if it is empty, set head and tail to LN
        ln = ListNode(value)

        if self.head is None:
            self.head = ln
            self.tail = ln

        else:
            self.head.prev = ln
            ln.next = self.head
            self.head = ln
        self.length += 1


        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
       # store the value of the head
        # decrement the length of the DLL
        # delete the head
            # if head.next is not None
                # set head.next's prev to None
                # set head to head.next
            # else (if head.next is None)
                # set head to None
                # set tail to None
        # return the value
        value = self.head.value
        self.delete(self.head)

        return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # LN with value
        #increment
        # if DLL empty
            # set head and tail to new node
        # if dll not empty
            # set new node prev to current tail
            # set tail's next  to new node
            # set tail  to new node
        if self.tail is None:
            self.tail = ListNode(value)
            self.head = self.tail    
        else:
            next_node = ListNode(value, self.tail)
            self.tail.next = next_node
            self.tail = next_node

        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store of tail
        # decrement
        # delete tail
            # if tail.prev is not None
                # set tail.prev's next to None
                # Set tail to tail.prev
            # else if tail.prev is None
                # set head and tail to none
        # return value
        temp_tail = self.tail
        self.length += -1
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head, self.tail = None, None
        return temp_tail.value
            

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # connect prev.next to current.next
        # connect next.prev to current.prev
        prev = node.prev
        prev.next = node.next
        next_node = node.next
        if node.next:
            next_node.prev = prev
        self.add_to_head(node.value)
        self.length += -1

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.add_to_tail(node.value)
        self.delete(node)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None:
            return

        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length += -1
        
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.length += -1

        elif node == self.tail:
            node.remove_from_tail()
        else:
            prev = node.prev
            prev.next = node.next
            next_node = node.next
            next_node.prev = prev
            self.length += -1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Create a current_max and current_current node to iterate through and compare
        current_max = 0
        current_node = self.head
        while current_node:
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max