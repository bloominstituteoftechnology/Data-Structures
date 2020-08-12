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
        Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if the node exists
        if self.head is None and self.tail is None:
            # if it doesnt, we're done
            return None
        # if the node exists
        else:
            # if the node to delete is the head node, make next node the head
            if self.head is node:
                self.head = node.next
            if self.tail is node:
                self.tail = node.prev
            # set the node's previous to point to the node's next
            if node.prev is not None:
                node.prev.next = node.next
            # set the node's next to point to the node's previous
            if node.next is not None:
                node.next.prev = node.prev
            # update length
            self.length += -1
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # wrap the value in a node
        new_node = ListNode(value)
        #check if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        #otherwise, the list has at least one node
        else:
            # set the old head's prev pointer
            self.head.prev = new_node
            #set the new head's next point to the old head
            new_node.next = self.head
            # set the head to point to the new node
            self.head = new_node
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #empty check
        if self.head is None and self.tail is None:
            return None

        # check if the linked list has only one node
        if self.head == self.tail:
            # store the value to remove
            val = self.head.value
            self.head = None
            self.tail = None
            self.length += -1
            return val
        #otherwise the DLL has more than one node
        else:
            #don't need to wrap anything , we're only removing and moving
            #save the removed node as a variable
            val = self.tail.value
            # make the prev. the new tail
            self.tail = self.tail.prev
            self.length += -1
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #wrap the value in a ListNode
        new_node = ListNode(value)
        #check if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        #otherwise, the DLL has at least one node so we just make the new tail
        else:
            #set the old tail's next point to new node
            self.tail.next = new_node
            #set the new tail's prev to the old tail
            new_node.prev = self.tail
            # set the new tail
            self.tail = new_node
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #empty check
        if self.head is None and self.tail is None:
            return None

        # check if the linked list has only one node
        if self.head == self.tail:
            # store the value to remove
            val = self.head.value
            self.head = None
            self.tail = None
            self.length += -1
            return val
        #otherwise the DLL has more than one node
        else:
            #don't need to wrap anything , we're only removing and moving
            #save the removed node as a variable
            val = self.tail.value
            # make the prev. the new tail
            self.tail = self.tail.prev
            self.length += -1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if the list is empty return None
        if(self.head is None):    
            print("List is empty") 
        else:
            # set a variable to use for list trasveral
            current = self.head
            #Initializing max to initial node data    
            maximum = self.head.value    
            while current is not None:    
                #If current node's data is greater than max    
                #Then replace value of max with current node's data    
                if(maximum < current.value):    
                    maximum = current.value    
                # set the current to the next node and run the above if
                # statement
                current = current.next
            print("Maximum value node in the list: "+ str(maximum)) 
            return maximum
   