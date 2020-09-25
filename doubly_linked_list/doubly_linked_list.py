"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def get_previous(self):
        return self.prev
    
    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_previous):
        self.prev = new_previous
    
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
        self.length += 1
        new_node = ListNode(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # set the new node's next to the current head
            new_node.set_next(self.head)
            # set the head's previous pointer to the new node
            self.head.set_previous(new_node)
            # set the head to the new node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.get_value()
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_node = ListNode(value)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else :
            # the previous should point to the old node
            new_node.set_previous(self.tail)
            #update the next node of the current node
            self.tail.set_next(new_node)
            # the tail should now point to the new node
            self.tail = new_node
            
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.get_value()
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.get_value()
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.get_value()
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        node.delete()
        self.length -= 1
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        # # Check to see if list is empty
        # if self.head is None and self.tail is None:
        #     return None
            
        # # decrement by 1
        # self.length -= 1

        # # Check to see if there is only one node 
        # if self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # # Check to see if it's the head node
        # elif node == self.head:
        #     self.head = node.next
        #     node.delete()
        # # Check to see if it's the tail node
        # elif node == self.tail:
        #     self.tail = node.prev
        #     node.delete()
        # else: 
        #     node.delete()

        
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_num = 0
        # starting from the head
        current_node = self.head

        # keep iterating until the node after "current_node" is the tail
        while current_node:
            #check the value with the current largest
            if current_node.get_value() > max_num:
                max_num = current_node.get_value()
            # keep looping
            current_node = current_node.get_next()

        return max_num

        