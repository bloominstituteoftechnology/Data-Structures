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
        # delete a node itself
        if self.prev:
            self.prev.next = self.next
        if self.next:
            next_node = self.next
            next_node.prev = self.prev

            
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
        # Create a node for the value
        new_node = ListNode(value)
        #check if the list is empty
        if self.head == None:
            #Store the new node that points to the head and tail
            self.head = new_node
            self.tail = new_node
        else: # list already has node in it 
            #set  next of the new node to the head and previous as Null
            new_node.next = self.head
            new_node.prev = None
            # move the head  to point new node
            self.head = new_node
        self.length +=1   



        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #check if the list is empty do nothing
        if self.head == None:
            return None
        value = self.head.value
        self.length -= 1
        if self.head ==self.tail:
            self.head =None
            self.tail =None
            return value
        else: 
            self.head.next = self.head
            self.head.prev =None
            return value



            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #Create a node for the value
        node = ListNode(value)
        #Check if the list is empty
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node
        self.length +=1   
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head == None:
            return None
        self.length -= 1   
        #check if list has one node 
        if self.head == self.tail: 
            value = self.head.value    
            self.head =None
            self.tail =None
            return value
        else:
            value =self.tail.value
            node = self.tail.prev 
            self.tail = node
            node.next =None  
            return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None:
            return None
        if self.head == node:
            return None
        else:
            old_value = node.value
            self.delete(node)
            self.add_to_head(old_value)
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head is None:
            return None
        if self.tail == node:
            return None
        else:
            old_value = node.value
            self.delete(node)
            self.add_to_tail(old_value)
             

        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check if the list is empty
        if self.head is None:
            return None
        #Check if list has only one node
        self.length -= 1
        value = node
        if self.head == self.tail:
            self.head =None
            self.tail =None
        #check if node is head
        elif self.head == node:
            self.head = node.next
            node.delete()
        #check if node is tail
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        # if node is some node in list
        else:
            node.delete()
        return value

        
            



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
           return None
        else:
            max_val =self.head.value
            current_node = self.head
            while current_node:
                if current_node.value > max_val:
                    max_val = current_node.value
                current_node = current_node.next
            return max_val
