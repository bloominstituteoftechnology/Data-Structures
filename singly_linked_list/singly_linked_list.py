"""
Implementations of linked lists and linked list nodes (value + pointer-to-next) 
as Python objects (classes).
"""

class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node (pointer to next node)
​
    Methods/Behavior/Operations:
    1. Get value
    2. Set value
    3. Get next node
    4. Set next node
    """

    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node
​
    Behavior/Methods:
    1. Add To Tail
    2. Prepend (Add a new node to head of the LL; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """

    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def prepend_to_head(self, value):
        # Make a new node using the input value:
        new_node = Node(value=value, next_node=None)
        # If the list is empty:
        if self.head is None:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # Else if we have a non-empty list, add the new node to the head:
        else:
            # wrap the input value in a node, which points to the existing head of the LL:
            new_node.set_next(self.head)
            # set the list's head reference to the new node
            self.head = new_node

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value=value, next_node=None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node
    
    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value
    
    def remove_tail(self):
        # If no nodes in linked list:
        if not self.head:
            return None
        
        # If 1 node in linked list:
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
    
        # Get value of existing tail node:
        value = self.tail.get_value()

        # Traverse the linked list to find the second-to-last node 
        # --> set as the new tail node:
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        self.tail = current
        self.tail.set_next(None)

        # Return value of old tail node:
        return value
    
    def contains(self, value):
        # Check if list is empty:
        if not self.head:
            return False
        
        # Recursive solution:
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False
    
    def get_max(self):
        # Check if list is empty:
        if not self.head:
            return None
        
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value


def reverse_ll(ll):
    """
    Reverse a singlu linked list.
    """
    current = ll.head
    previous = None
    while current is not None:
        # Store pointer to next node as variable:
        next_node = current.get_next()
        # Reverse pointer direction: Change current node's pointer to previous node:
        current.set_next(previous)
        # Move down the list 1 node:
        previous = current
        current = next_node
    # Switch the LL's head and tail pointers:
    ll.head, ll.tail = ll.tail, ll.head
    # Return the reversed list:
    return ll
    