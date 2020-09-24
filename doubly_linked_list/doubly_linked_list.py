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
        new_node = ListNode(value)
        
        if not self.tail and not self.head:
           
            self.head = new_node
            self.tail = new_node
       
        else:
           
            new_node.next = self.head
           
            self.head.prev = new_node
           
            self.head = new_node
       
        self.length += 1
        
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        
        self.length -= 1
       
        if self.head.next is not None:
           
            self.head.next.prev = None
            
            self.head = self.head.next
    
        else:
     
            self.head = None
       
            self.tail = None
    
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
       
        new_node = ListNode(value)
       
        if not self.tail and not self.head:
          
            self.head = new_node
            self.tail = new_node
        
        else:
          
            new_node.prev = self.tail
           
            self.tail.next = new_node
           
            self.tail = new_node
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
       
        if self.tail.prev is not None:
           
            self.tail.prev.next = None
          
            self.tail = tail.prev 
       
        else:
          
            self.head = None
            
            self.tail = None
       
        self.length -= 1

        return value
        
    

             
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        
        if node is self.head:
           
            return
       
        if node is self.tail:
            
            self.tail = self.tail.prev
       
        node.prev.next = node.next
        
        if node.next is not None:
            
            node.next.prev = node.prev 
        
        node.prev = None
       
        node.next = self.head
        
        self.head.prev = node
  
        self.head = node
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            
            return None
       
        if node is self.head:
            
            self.head = self.head.next
       
        node.next.prev = node.prev
        
        if node.prev is not None:
            
            node.prev.next = node.next
    
        node.next = None
        
        node.prev = self.tail
        
        self.tail.next = node
        
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return None

        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                node.next.prev = node.prev
                self.head = node.next
            elif node is self.tail:
                node.prev.next = node.next
                self.tail = node.prev
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
        self.length -= 1
            
       

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None

        current = self.head
        max_value = current.value
        while current.next is not None:
            if max_value < current.next.value:
                max_value = current.next.value
            current = current.next
        return max_value