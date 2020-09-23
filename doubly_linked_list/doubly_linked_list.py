"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def next_node(self):
        return self.next

    def prev_node(self):
        return self.prev

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
        # create instance of new DLL node
        new_node = ListNode(value, None, None)

        # increment the list length
        self.length +=1

        # check for empty list, and makes the new node both head and tail if it is the only node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # otherwise points the current head at the new node as the new head of the list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check for list
        if self.head is None:
            return None
        # save value of head node
        value = self.head.value

        # call delete on the head node
        self.delete(self.head)

        # return the value of the head node
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # adds a new instance of DLL node class with given value
        new_node = ListNode(value, None, None)

        # increment list length
        self.length += 1

        # checks for empty list and makes the new node both the head and tail of the new list
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        # otherwise points the current tail at the new node which becomes the tail of the list
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
        # check if there is a list
        if self.tail is None:
            return None
        # save the value of the tail
        value = self.tail.value
        # delete the tail
        self.delete(self.tail)
        # return tail value
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # check if node is already head
        if node is self.head:
            return

        # save value of current node
        value = node.value

        # check edge case if node is tail and calls the delete tail method
        if node is self.tail:
            self.delete(self.tail)
        else:
            # if any other node, calls delete method
            self.delete(node)

        # calls add to head method with saved value
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check edge case if node is already tail
        if node is self.tail:
            return

        # save value of current node
        value = node.value
        # call delete method on current node
        self.delete(node)
        # call add to tail method with saved value for the node we just deleted
        self.add_to_tail(value)
      

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # decrement list length
        self.length -= 1
        
        # check for edge case of no list
        if self.head is None or node is None:
            return None
        
        # check if node is head of list
        if self.head == node:
            self.head = node.next
            # call delete method on node class
            node.delete()
        
        # check if node is tail of list
        if self.tail == node:
            self.tail = node.prev
            # call delete method on node class
            node.delete()
        else:
            node.delete()
            
      
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # check for empty list
        if self.head is None:
            return None
        # set the current pointer to the next node in line
        current = self.head.next
        # set the max value to the value of the current node
        maximum = self.head.value
        while current:
            # check the value of the current node against maximum value 
            if current.value > maximum:
                # #update the max value if current is larger than latest maximum
                maximum = current.value
            # move the current node to the next node in line
            current = current.next
        # return maximum node value
        return maximum

