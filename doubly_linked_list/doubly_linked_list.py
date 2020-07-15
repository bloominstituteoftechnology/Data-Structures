# doubly_linked_list/doubly_linked_list.py

"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next_ = next_

    def get_value(self):
        self.value

    def get_next_(self):
        return self.next_

    def set_next_(self, new_node):
        self.next_ = new_node

    def get_prev():
        return self.prev      

    def set_prev(self, new_node):
        self.prev = new_node

    def delete(self):
        if self.prev:
            self.prev.next_ = self.next_
        elif self.next_:
            self.next_.prev = self.prev
        
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
        self.length += 1

        # Adding node to an empty list:
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Adding node to a non-empty list:
        else:
            new_node.next_ = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    # def remove_from_head(self):
    #     if self.head is None and self.tail is None:
    #         return None

    #     elif self.head is self.tail:
    #         value = self.head.value
    #         self.head = None
    #         self.tail = None
    #         self.length -= 1
    #         return value
    
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # Adding node to an empty list:
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        # Adding node to a non-empty list:
        else:
            new_node.prev = self.tail
            self.tail.next_ = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
            
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
        # deleting from empty list:
        if self.head is None and self.tail is None:
            return
        # deleting from a single-node list:
        elif self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # deleting the head node, self.list >= 2
        elif node == self.head:
            self.head = node.next_
            node.delete()
        # deleting the tail node, self.list >= 2
        elif node == self.tail:
            self.tail = node.prev
            node.delete()
        # general case node
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    # def get_max(self):
        # if not self.head or not self.tail:
        #     return None

        # max_value = self.head.get_value()

        # current = self.head.get_next_()
        # while current:
        #     if current.get_value() > max_value:
        #         max_value = current.get_value
        #     current.get_next_()
        # return max_value




