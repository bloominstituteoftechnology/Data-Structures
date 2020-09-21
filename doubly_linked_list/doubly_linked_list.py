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
        pass
        self.length +=1
        node =  ListNode(value)
        if self.head == None:
            self.head = node
            self.tail = node 
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        if self.head == None:
            return None
        node = self.head
        self.length -=1 
        self.head = node.next
        if self.head == None:
            self.tail = None
        else:
            self.head.prev = None
        return node.value   
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
        self.length +=1
        node =  ListNode(value)
        if self.tail == None:
            self.head = node
            self.tail = node 
        else:
            node.prev = self.tail
            self.tail.next = node 
            self.tail = node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
        if self.tail == None:
            return None
        node = self.tail
        self.length -=1
        self.tail = node.prev
        print("Quote Tail", self.tail)
        if self.tail == None:
            self.head = None
        else:
            self.tail.next = None
        return node.value

   
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
    #disloging code:
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev 
        if self.tail == node:
            self.tail = node.prev

        node.next = self.head
        self.head.prev = node
        self.head = node


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass
    #disloging code:
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev 
        if self.head == node:
            self.head = node.next
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass
        self.length -= 1

        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev 
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
        max_value = self.head.value
        node = self.head
        while node != None:
            if node.value > max_value:
                max_value = node.value
            node = node.next
        return max_value
