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
        self.head = None
        self.tail = None
            
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
        # Create the Node from the value
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            # have both head and tail refer to a single node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            # reassign self.head to refer to the new node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        # 
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create the Node from the value
        node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            # have both head and tail refer to a single node
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            # reassign self.tail to refer to the new Node
            self.tail = node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        # Delete the current node
        self.delete(self.tail)
        # return the value of the removed node
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        # Delete the node from its current spot
        self.delete(node)
        # add the node to the head
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        # Delete the node
        self.delete(node)
        # add the node to the tail
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        if not self.head and not self.tail:
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            node.delete()
        elif node == self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = None
        node = self.head
        while node:
            if not max:
                max = node.value
                # if current node's data is greater than max, then replace value of max with current node's data
            elif node.value > max:
                max = node.value
            node = node.next
        return max
