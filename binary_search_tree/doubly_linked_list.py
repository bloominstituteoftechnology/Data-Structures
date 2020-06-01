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
            
    def iterate_list(node):
        while none is not None:
            print(node.value)
            node = node.next


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    #find middle
    def find_middle(self):
        middle = self.head
        end = self.head
        
        while end != None and end.next.next != None:
            end = end.next
            middle = middle.next
        
        print(middle)
        return middle

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap given value in list node
        new_node = ListNode(value, None, None)
        self.length += 1
        #handle if list has a head
        if self.head:
            new_node.next = self.head # points new node to the old head
            self.head.prev = new_node # point the old head to the new node
            self.head = new_node #set the new head            
        
        #handle if list has no head
        else:
            self.head = new_node #set new head
            self.tail = new_node #set new node as tail because it doesn't point to another node
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        
        return value
        
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        
        #handle if list has a tail
        if self.tail:
            self.tail.next = new_node #point existing tail to the new node
            new_node.prev = self.tail #points to the current tail
            self.tail = new_node #sets the new tail
        
        #handle if list has no tail
        else:
            self.head = new_node #sets new head
            
        self.tail = new_node #sets new tail
        
           
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        #if head and tail are same
        if self.head == self.tail:
            self.head = None
            self.head = None
            
        #if 0 nodes
        if not self.tail:
            return        
        
        #if more than one node
        else:
            
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.length -= 1
        
        return value       
       
       
         

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # delete
        self.delete(node)
        new_node.next = self.head # points new node to the old head
        self.head.prev = new_node # point the old head to the new node
        self.head = new_node #set the new head   
        
        # the add_to_head
        self.add_to_head(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # delete
        # then add_to_tail
        value = node.value
        self.delete(node)
        self.add_to_tail(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
               
        # if list is empty
        if not self.head:
            print("Do nothing")
            return
        
        self.length -= 1
        
        # if list has one item
        if self.head == self.tail:
            self.head = None
            self.tail = None
            
        #if list has at least 2 nodes, and we want to delete the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        
        
        # if list has at least 2 nodes, and we want to delete the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # walk through entire list
        # keep track of biggest value we have found
        
        highest_value = self.head.value
        current_node = self.head
        
        while current_node is not None:   
            if current_node.value > highest_value:
                highest_value = current_node.value
            current_node = current_node.next
            
        return highest_value
