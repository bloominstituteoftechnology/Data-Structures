from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self, head: Optional[Node] = None, tail: Optional[Node] = None):
        self.head = head
        self.tail = tail
    
    def insert_at_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node


    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def contains(self, value) -> bool:
            # Traverse through list, checking values
            node = self.head

            while node is not None:
                if node.value == value:
                    return True
                node = node.next

            return False
            
    def remove_head(self):
        # What if we have no nodes?
        # What if we only have one node?
        
        if self.head is None:
            return
        else :
            value = self.head.value

            if self.tail == self.head:
                self.tail = None
            self.head = self.head.next

            return value

    def remove_tail(self):
        # We have a pointer to the tail, the only problem is that 
        # if we just remove the tail, the node before it won't be updated to point to None
        # Thus, we need to iterate through all the nodes until we get to the node *before* the tail
        # We will always be looking ahead to the next node to make sure we don't go too far
        # Whe we get to the node before, we will grab a reference to the tail, so we can return it's value
        # We will then set the node before the tail as the new tail
        # and set it's next as None
        # then return the old tail's value
        # This opertion will take O(n) time, as it has to iterate through all nodes

        # Before doing all this, we need to check for two special cases
        
        # First, let's make sure there is a tail
        if not self.tail:
            return # nothing to return if there is no tail

        # Next, let's check if there is only one node
        if self.tail == self.head:
            tail = self.tail # grab a reference
            self.tail = None # zero out tail
            self.head = None # and head, since they are the same node
            return tail.value # return the tail's value

        current_node = self.head # start with current node as the head

        while current_node.next.next != None: # looking ahead
            current_node = current_node.next # if next isn't tail, advance
        
        tail = current_node.next # now we know that the next node is the tail, grab a reference to it for returning
        self.tail = current_node # move our tail pointer back one spot to the current node
        current_node.next = None # set current node's next to None
        return tail.value # finally, return the value of the tail
         
    def get_max(self):
        max = None
        node = self.head

        while node is not None:
            if max is None:
                max = node.value
            elif node.value > max:
                max = node.value

            node = node.next
        
        return max

