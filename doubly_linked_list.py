	"""
	ListNode `delete` method 
	"""
	def delete(self):
        if self.prev:
                self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
	
	"""
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # is there anything to delete?
        if self.head is None and self.tail is None:
            return
        # check if there's only one node 
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # check if the node is the head 
        elif node is self.head:
            self.head = node.next
            node.delete()
        # check if the node is the tail 
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # otherwise, the node is some node in the middle 
        else:
            node.delete()
        # don't forget to decrement the length 
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if the list is empty, return None 
        if self.head is None and self.tail is None:
            return
        # keep track of the largest value we've seen so far 
        max_value = self.head.value
        # traverse the entirety of the linked list 
        current = self.head.next
        
        while current is not None:
            # if we see a value > the largest value we've seen so far 
            if current.value > max_value:
                # update the largest value 
                max_value = current.value
            # update current to point to the next node 
            current = current.next
        # return the largest value 
        return max_value