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
        if self.length == 0:
            new_node = ListNode(value=value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value, next=self.head)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length +=  1
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return val
           
        
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return node.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == None or self.length == 0: 
            new_node = ListNode(value=value)
           
            self.head = new_node
            self.tail = new_node
        else:

            
            new_node = ListNode(value, prev=self.tail,)
            
            self.tail.next = new_node
            
            self.tail = new_node 
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            self.tail = None
            self.head = None
            return None
      
        node = self.tail
        self.tail = self.tail.prev
        if self.length == 1:
            self.head  = None
        if self.tail is not None:
            self.tail.next = None
      
        self.length -= 1
        return node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length <= 1:
            return
     
        prev_node = node.prev
        next_node = node.next
       
        if prev_node is not None:
            prev_node.next = next_node
        else:
            
            return
        if next_node is not None:
            next_node.prev = prev_node
        else:
           
            self.tail = self.tail.prev
            self.tail.next = None
       
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length <= 1: 
            return 
       
        prev_node = node.prev
        next_node = node.next
       
        if prev_node is not None:
            prev_node.next = next_node
        else:
            
            self.head = self.head.next
            self.head.prev = None
        if next_node is not None:
            next_node.prev = prev_node
        else:
            
           
            return
        
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail  = node
        return


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
    
        if self.length == 0:
            return None
       
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length = 0
            return node.value
       
        prev_node = node.prev
        next_node = node.next
       
        if prev_node is not None:
            prev_node.next = next_node
        else:
           
            self.head = self.head.next
            self.head.prev = None
        if next_node is not None:
            next_node.prev = prev_node
        else:
            
            self.tail = self.tail.prev
            self.tail.next = None
      
        self.length -= 1

        return node.value


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
      
        if self.length == 0:
            return None
       
        val = self.head.value
      
        node = self.head
        while True:
            if node.value > val:
                val = node.value
           
            if node.next == None:
                return val
            node = node.next
        return val


1