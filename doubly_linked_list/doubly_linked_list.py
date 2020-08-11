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
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            #set head and tail to the new node
            self.head = new_node
            self.tail = new_node
            #otherwise the list has at least one node
        else:
            #update the last node's 'next_node' to the new node
            
            new_node.next = self.head
            old_head = self.head
            old_head.prev = new_node
            self.head = new_node
            self.length += 1

            
    
        #1. wrap the value in a list node
        #2. check if dll is empty, set head and tail to refer to new_node
        #3. otherwise dll is not empty
        # - set head to new node, new_node's next needs to point to old head.
        # set old head's next needs to point to new_head 
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
            # #update the last node's 'next_node' to the new node
            # # old_head = self.head
            # # new_head = old_head.next
            # # new_head.next = old_head.next
            # # delete(old_head)
            # # new_node.next = self.head
            # # old_head = self.head
            # # old_head.prev = new_node
            # # self.head = new_node
            # # self.length -= 1
            # values = self.head.value
            # self.head = self.head.next
            # if self.head != None:
            #     self.head.prev = None
            # self.length -= 1
            # return values
        if(self.head == None):    
            return;    
        else:    
               
            if(self.head != self.tail):
                value = self.head.value    
                self.head = self.head.next;    
                self.head.prev = None;    
                self.length -= 1
                return value
            else:    
                self.head = self.tail = None;  
                self.length -= 1
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if (self.length == 0):
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
        values = self.tail.value
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        self.length -= 1
        
        return values
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            return node
        DoublyLinkedList.delete(node)
        DoublyLinkedList.add_to_head(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return node
        #doesn't work because add to tail requres a value argument and delete wants a node
        #not sure how to work around that
        DoublyLinkedList.add_to_tail(node)
        DoublyLinkedList.delete(node)
        
        

        #1. is the input node already the tail?
        #2. Remove the node in question, add it as the tail
        # -use delete method to remove node in question
        # add to tail method
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        pass
        #need to make sure 4 no longer has arrows pointing at it
        #redirect arrows pointing at 4,
        #take arrow pointing from 4's previous, make it point to 4's next
        #take arrow pointing from 4's next, set it to 4's previous
        #needs to no longer have references pointing to it
        
        #set node's previous to point to node's next
        #set node's next to point to node's previous
        #node.prev.next = node.next
        #node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass