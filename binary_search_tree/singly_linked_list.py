
class Node:
    """
    A Node to use in a LinkedList
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        """
        Method to get the value of the node
        """
        return self.value
    
    def get_next(self):
        """
        Method to get the node's `next_node`
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's `next_node` to `new_next`
        """
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        # check if empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # otherwise must have at least one
        else:
            # update the last node's `next_node` to the new node
            self.tail.set_next(new_node)
            # update the `self.tail` to point to the new node that we just added
            self.tail = new_node
        
    def remove_tail(self):
        """
        Remove the last node in the chain and return its value
        """
        # check for empty list
        if self.head is None and self.tail is None:
            return None

        # check if list only has one item
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            # set the head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        
        # otherwise
        else:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()

            # set the `self.tail` to the second-to-last node
            # we can only do this by traversing the whole list from beginning to end
            
            # start from the head
            current_node = self.head

            # keep iterating until the node after `current_node` is the tail
            while current_node.get_next() != self.tail:
                # keep looping
                current_node = current_node.get_next()

            # at the end of iteration set `self.tail` to the `current_node`
            self.tail = current_node
            # set the new tail's `next_node` to None
            self.tail.set_next(None)
            # return 
            return value

    def remove_head(self):
        # check for empty list
        if self.head is None and self.tail is None:
            return None

        # check if list only has one item
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            # set the head and the tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        else:
            # store the old head's value
            value = self.head.get_value()
            # set self.head to old head's next
            self.head = self.head.get_next()
            # return the value
            return value