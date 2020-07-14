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
        self.value = None
        pass
            
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
        # Create instance of ListNode with value
        new_node = ListNode(value)

        # Increment the DLL Length Attribute
        self.length += 1

        # Check if DLL is empty
            # If it is empty: 
                # Set head and tail to the new node instance
        if self == None:
            self.head = new_node
            self.tail = new_node

            # If not:
                # Set new nodes next to current head
                # Set head's previous to new node
                # Set head to new node head
        else:
            new_node.next = self.head
            self.prev = new_node
            self.head = new_node.value
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Store the Value of the Head
        removed = self.head
        # Decrement Length
        self.length -= 1
        # Delete the Head
        removed.delete()
            # If current Head's next is not None
                # Set next node's previous value to None
                # Set head to current Head's next value
        if removed.next != None:
            new_head_node = removed.next
            new_head_node.prev = None
            removed.next = None
            removed = new_head_node.head

            # Else if Head is None
                # Set Head to None
                # Set Tail to None
        else:
            removed = None
            self.tail = None

        # Return the Value
        return removed
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create instance of ListNode with value
        new_node = ListNode(value)
        # Increment the DLL Length Attribute
        self.length += 1

        # Check if DLL is empty
            # If it is empty: 
                # Set head and tail to the new node instance
        if self == None:
            self.head = new_node
            self.tail = new_node

        # If DLL is NOT empty:
            # Set new node's previous to the current tail
            # Set Tail's Next to new node
            # Set Tail to New node
        else:
            new_node.prev = self.tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Store the Value of the Tail
        removed = self.tail
        # Decrement Length
        self.length -= 1
        # Delete the Tail
        removed.delete()
            # If current Tail's previous is not None
                # Set head node's next value to None
                # Set tail to current Head's next value
        if removed.prev != None:
            head_node = removed.prev
            head_node.next = removed

            # Else if tail.prev is None
                # Set Head to None
                # Set Tail to None
        else:
            removed = None
            self.head - None

        # Return the Value
        return removed
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass