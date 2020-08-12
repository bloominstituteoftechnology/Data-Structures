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

        #  new_node = ListNode(value)

        # if self.head and self.tail:
        #     new_node.next = self.head
        #     self.head.prev = new_node

        #     self.head = new_node
        # else:
        #     self.head = new_node
        #     self.tail = new_node

        # self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

       removed_node = self.head # store the node we want to delete

        # check to see if there is a head.  If not, return None.
        if not self.head:
            return None

        self.head.delete() # delete the node.
        self.head = removed_node.next # set new node as head
        self.tail = None # set tail reference to None (or tests fail)
        self.length -= 1

        return removed_node.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # initalize a new node with prev and next as None:
        new_node = ListNode(value, None, None)

        # check if the DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail # new_nodes prev is now pointing to current tail
            self.tail.next = new_node # current tail's next is now pointing to new_node
            self.tail = new_node # new_node is now the tail

        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value # store the node we want to delete

        if not self.tail:  # if there isn't a tail, do nothing and return None.
            return None

        # if there is a tail our delete method which sets new pointers.
        self.delete(self.tail)

        return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check to see if the node is already the head.  If yes, do nothing and return node.
        if node is self.head:
            return node

        if node is self.tail:
            self.remove_from_tail()
        else:
            self.delete(node) # delete our old node.

        self.add_to_head(node.value) # call our add to node method
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # If already at tail, just return the value.
        if node is self.tail:
            return node

        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # is there anything to delete?
        if self.head is None and self.tail. is None:
            return
        # check if theres only one node
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # check if node is the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # check if node is the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # check if node is in the middle
        else:
            node.delete()
        # dont forget to decrement the length
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if the list is empty, return None
        if self.head is None and self.tail is None:
            return
        # keep track of the largest value weve seen so far in a variable
        max_value = self.head.value
        # traverse the entirerity of the linked list
        current = self.head.next

        while current is not None:
            #  if we see a value > the largest value wever seen so far
            if current.value > max_value:
            # update the largest value
                max_value = current.value
            # update current point to the next node
            current = current.next
        # return the largest value
        return max_value