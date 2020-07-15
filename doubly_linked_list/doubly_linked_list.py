"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
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

        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
            # set head an tail to the new node instance
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("node inserted")
            return
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        value = self.head.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
            # if next is not None
                # set head.next.prev to None
                # set head to head.next

        # return the value
        if self.head is None:
            print("The list has no element to delete")
            return None
        if self.head.next is None:
            self.head = None
            self.tail = None
            return value
        else:
            self.head = self.head.next
            self.head.prev = None
            return value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
            # set head an tail to the new node instance
        # if DLL is not empty
            # set new node's prev to current head
            # set tail's next to new node
            # set tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.prev = self.head
            self.tail.next = new_node
            self.tail = new_node
            return
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the head
        value = self.head.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
            # if tail.prev is not None
                # set tail.prev.next to None
                # set tail to tail.prev
        # return the value
        if self.head is None:
            print("The list has no element to delete")
            return None
        if self.tail.prev is None:
            self.head = None
            self.tail = None
            return value
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return value
            
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
        self.length -= 1
        if self.head is None or node is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == node: 
            self.head = node.next
  
        # Change next only if node to be deleted is NOT 
        # the last node 
        if node.next is not None: 
            node.next.prev = node.prev
            node.prev = node.next 
      
        # Change prev only if node to be deleted is NOT  
        # the first node 
        if node.prev is not None: 
            node.prev.next = node.next

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head    
        #Initializing max to initial node data    
        maximum = self.head.value  
        if self.head != None:    
            while True:    
            #If current node's data is greater than max    
            #Then replace value of max with current node's data    
                if maximum < current.value:    
                    maximum = current.value    
                    current= current.next    
                if current == self.head:    
                    return    
