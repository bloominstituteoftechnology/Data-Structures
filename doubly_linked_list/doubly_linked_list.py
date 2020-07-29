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
        # create a node
        new_node = ListNode(value)

        # check if list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node

        # establish new relationships then reassign the head
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check empty
        if not self.head:
            return None
        
        # decrement
        self.length -= 1
        
        if self.head == self.tail:
            head = self.head.value
            self.head = None
            self.tail = None
            return head

        # reassign head and return value
        head = self.head.value
        self.head = self.head.next

        return head            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a node
        new_node = ListNode(value)

        # check if list is empty
        if not self.tail:
            self.head = new_node
            self.tail = new_node

        # establish new relationships then reassign the tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # check empty
        if not self.tail:
            return None
        
        # decrement length
        self.length -= 1

        # check if singular list
        if self.tail == self.head:
            tail = self.tail.value
            self.head = None
            self.tail = None
            return tail
        
        # reassign and return value
        tail = self.tail.value
        self.tail = self.tail.prev

        return tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if passed node is already the head
        if self.head == node:
            return 

        # delete passed node from list and add to head
        self.delete(node)
        self.add_to_head(node.value)   
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if passed node is already the head
        if self.tail == node:
            return

        # delete passed node from list and add to tail
        self.delete(node)
        self.add_to_tail(node.value)   

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #check legnth before decrement
        if self.length > 0:
            self.length -= 1
        #check empty
        if self.head is None:
            return
        #check singular list
        elif self.head == self.tail == node:
            self.head = None
            self.tail = None
        #check if passed node is head or tail
        elif self.head == node:
            self.head = self.head.next
        elif self.tail == node:
            self.tail = self.tail.prev
        #otherwise search and destroy
        else:
            # placeholder to start at item 2
            current = self.head.next

            # traverse list
            while current:
                if current == node:
                    current.delete()
                    break
                current = current.next
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self): 
        # check for empty list     
        if not self.head:
            return None
        
        # set initial values
        max_val = 0
        current = self.head

        # iterrate through list
        while current:
            current_val = current.value

            # compare values and update max when greater value presented
            if max_val < current_val:
                max_val = current_val

            current = current.next

        return max_val