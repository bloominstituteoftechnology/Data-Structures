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
        #   Create instance of ListNode w/ Value
        #   Increment the DLL length attribute

        #   Check if DLL is empty
            #   if it is empty
            #   set head and tail to the new node instance

        #   If DLL is not empty
            #   set new node's next to current head
            #   set head's prev to new node
            #   set head to the new node
        current_head = self.head
        #   If head exists
        if self.head:
            self.head = ListNode(value, None, current_head)
            current_head.prev = self.head
        #   If head does not exist then tail does not exist. Must assign new node to head AND tail.
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #   Store the value of the head
        #   Decrement the head
        #   Delete the head
            #   if head.next is not None
                #   set head.next's prev to None
                #   set hed to head.next

        #   Return the value

        #   If head exists
        if self.head:
            current_head = self.head
            #   If there is only one node both head and tail should be None
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head.delete()
                self.head = current_head.next
                self.length -= 1

            return current_head.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #   Create instance of ListNode with value
        #   Increment the DLL length attribute

        #   If DLL is empty
            #   set head and tail to the new node instance

        #   If DLL is not empty
            #   set new node's prev to current tail
            #   set tail's next to new node
            #   set tail to the new node


        #   If tail exists
        if self.tail:
            newNode = ListNode(value, self.tail)
            self.tail.next = newNode
            self.tail = newNode
            #   Tail does not exist then head does not exist
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        
        #   Store the value of the tail
        #   Decrement the length of the DLL
        #   Delete the tail
            #   if tail.prev is not None
                #   set tail.prev's next to None
                #   set tail to tail.prev
            #   els (if tail.prev is None)
                #   set head to None
                #   set tail to None

                #   Return the value

        #   If tail exists
        current_tail = self.tail
        if self.tail:            
            self.length -=1
            if self.tail == self.head: 
                #   --or--  self.length ==1
                    self.tail = None
                    self.head = None
            else:
                    self.tail = current_tail.prev
                    self.tail.next = None
        if current_tail:
            return current_tail.value
        else:
            return None
                
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #   Always check if exists
        if self.head:
            node.delete()
            current_head = self.head
            self.head = node
            self.head.next = current_head
            current_head.prev = self.head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #   Check if tail exists
        if self.tail:
            self.remove_from_head()
            current_tail = self.tail
            self.tail = node
            current_tail.next = self.tail
            self.tail.prev = current_tail
            self.length += 1
        else:

            current_tail = self.tail
            node.delete()
            self.tail = node
            current_tail.next = self.tail
            self.tail.prev = current_tail
            

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -=1


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current_node = self.head
        max_value = self.head.value
        for i in range(1,self.length):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value