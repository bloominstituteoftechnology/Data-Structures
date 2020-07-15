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
        if self.head and self.tail:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # here if we don’t have head then it’s return none
        if self.head is None:
            return None
        # current value is self.head
        current = self.head
        # here we are looking for while loop which is current next if not equal to tail then current is going to keep going next.
        while current.next and current.next is not self.tail:
            current = current.next
        # if found we get the tail value.
        value = self.tail.value
        # current.next = none so we are deleting
        current.next = None
        self.tail = current
        # here we are making it to assign current which converted to None
        # we return the value.
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail and self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

        self.length += 1


    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        current = self.tail
        while current.next and current.next is not self.head:
            current = current.next

        value = self.head.value
        current.next = None
        self.head = current
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            return
        else:
            temp = self.head.value
            self.add_to_head(temp)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            temp = None
            temp = self.tail.value
            self.add_to_tail(temp)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.tail:
            # here we are leaving the node.
            self.tail.prev
        elif node == self.head:
            # here we are also leaving the node.
            self.head.next
        # by this length -1 we are decreasing a node from traverse.
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_ = self.value
        for item in max_:
            if item > max_:
                max_ = item
        return max_