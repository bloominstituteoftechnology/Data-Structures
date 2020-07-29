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
        # create a new list node instance
        new_node = ListNode(value)
        self.length += 1

        # check to see if the list is empty
        if self.head is None and self.tail is None:
            # assign the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else: 
            # if there is one or more element than reassign the head
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
  
    def add_to_tail(self, value):
        self.length += 1
        # initialize the new list node
        new_node = ListNode(value)
        # check if the list is empty
        if not self.head:
            self.head == new_node
            self.tail == new_node 
        # if there one or more element on the list
        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node 


    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
         
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if the list is empty
        if self.head is None: 
            return None
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None:
            return None
        if node is self.tail:
            return 
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # check to see if the list is empty
        if self.head is None and self.tail is None: 
            return 
        self.length -= 1
        # if there is just one element in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if the node is the head
        elif self.head == node:
            self.head = node.next
            node.delete()
        # if the node is tail
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
        # check if the list is empty
        if not self.head:
            return None
        # check if there is only one element
        if self.head is self.tail:
            return self.head.value
        # if there are more than one element in the list
        max_num = self.head.value
        current_node = self.head
        # loop until there is nothing on the list
        while current_node is not None:
            if current_node.value > max_num:
                max_num = current_node.value
            current_node = current_node.next
        return max_num

        