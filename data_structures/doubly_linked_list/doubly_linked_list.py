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
        if self.length == 0: # there are no nodes yet
            new_node = ListNode(value=value)
            # assigning the Double linked list to the newNode
            self.head = new_node
            self.tail = new_node
        else:

            # if there is already a node in the list then will do the following
            new_node = ListNode(value, next=self.head)
            # now assigning the previous tail to the new_node
            self.head.prev = new_node
            new_node.next = self.head
            # making the head point to the new_node
            self.head = new_node
        # incremetig the length
        self.length +=  1
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return val
           
        # will remove the head now if there is one
        # Need to check 
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        # decrementing the size of the linked list
        self.length -= 1
        return node.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == None or self.length == 0: # there are no nodes yet
            new_node = ListNode(value=value)
            # assigning the Double linked list to the newNode
            self.head = new_node
            self.tail = new_node
        else:

            # if there is already a node in the list then will do the following
            new_node = ListNode(value, prev=self.tail,)
            # now assigning the previous tail to the new_node
            self.tail.next = new_node
            # making the tail point to the new_node
            self.tail = new_node 
        # incrementing
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            self.tail = None
            self.head = None
            return None
        # below will remove the tail if there is one
        node = self.tail
        self.tail = self.tail.prev
        if self.length == 1:
            self.head  = None
        if self.tail is not None:
            self.tail.next = None
        # decrementing the size 
        self.length -= 1
        return node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length <= 1:
            return
        # putting the node into the front
        prev_node = node.prev
        next_node = node.next
        # linking the nodes together
        if prev_node is not None:
            prev_node.next = next_node
        else:
            # if in here means that it is already in the front
            return
        if next_node is not None:
            next_node.prev = prev_node
        else:
            # if in here means the the node is the tail
            self.tail = self.tail.prev
            self.tail.next = None
        # putting the node at the front
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length <= 1: 
            return 
        # below will be putting the node at the end
        prev_node = node.prev
        next_node = node.next
        # linking them together
        if prev_node is not None:
            prev_node.next = next_node
        else:
            # That would mean that we need to change the head
            self.head = self.head.next
            self.head.prev = None
        if next_node is not None:
            next_node.prev = prev_node
        else:
            # this means that the node asked to move is 
            # already at the end
            return
        # adding the node to the tail
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail  = node
        return


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # will check to see if there are none
        if self.length == 0:
            return None
        # checking to see if the length is 1
        if self.length == 1:
            self.tail = None
            self.head = None
            self.length = 0
            return node.value
        # doing the deleting of the node here if there are at least two nodes
        prev_node = node.prev
        next_node = node.next
        # doing the linking of the nodes
        if prev_node is not None:
            prev_node.next = next_node
        else:
            # if in here it means that we are deleting the head
            self.head = self.head.next
            self.head.prev = None
        if next_node is not None:
            next_node.prev = prev_node
        else:
            # if in here means that we are deleting the tail
            self.tail = self.tail.prev
            self.tail.next = None
        # decrementing the list
        self.length -= 1

        return node.value


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # checking to see if there is any thing in the list
        if self.length == 0:
            return None
        # doing the looping through the list to find the max
        val = self.head.value
        # setting to look at a node
        node = self.head
        while True:
            if node.value > val:
                val = node.value
            # moving to the next node
            if node.next == None:
                return val
            node = node.next
        return val


    
    # This is a method that I made to print out the list of the doulble linked list
    # from the head to the tail
    def printList(self):
        if self.length == None or self.length == 0:
            print("The Double linked list is empty\n")
        else:
            node = self.head
            while True:
                print(node.value, "\n")
                if node.next == None:
                    break
                else:
                    node = node.next