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
        # create instance of ListNode with value
        new_node = ListNode(value, None, None)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        value =self.head.value
        # decrement the length of the DLL
        #self.length -= 1
        # delete the head
        self.delete(self.head)
        # # if head.next is not None
        # if self.head.next is not None:
        #     # set head.next's prev to None
        #     self.head.next.previous = None
        #     # set head to head.next
        #     self.head = self.head.next
        # # else (if head.next is None)
        # else:
        #     # set head, tail to None
        #     self.head = self.tail = None
        # # return the value
        return value
      
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value, None, None)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if not self.tail and not self.head:
            # set head and tail to the new node instance 
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node  
            self.tail = new_node
         
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # store the value of the tail
        value = self.tail.value
        # decrement the length of the DLL
        #self.length -= 1
        # delete the tail
        self.delete(self.tail)
        # # if tail.prev is not None
        # if self.tail.previous != None:
        #     # set tail.prev's next to None
        #     self.tail.prevoius.next = None
        #     # set tail to tail.prev
        #     self.tail = self.tail.previous
        # # else (if tail.prev is None)
        # else:
        #     # set head to None
        #     self.head = None
        #     # set tail to None
        #     self.tail = None
        # # return the value          
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)   
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -=1
            self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -= 1
        if self.head is self.tail:
            self.head = self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
