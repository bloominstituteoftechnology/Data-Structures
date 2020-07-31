class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value



# The linked list will use the nodes and then will make the linked list

class LinkedList():
    def __init__(self):
        # Getting the info that will be stored ready to be used
        self.head = None # The head and the tail will 
                         # both eventually store a node
        self.tail = None
        self.length = 0  # I will be using the lenth to help
                         # help with my linked list class


    # method the add to the tail
    def add_to_tail(self, value):
        new_node = Node(value=value)
        
        # Checking to see the length of the linked list
        if self.length == 0:
            # here head and the tail are the same
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            # now assigning the newNode to be the tail
            self.tail = new_node
        # incrementing the length
        self.length += 1
        

    def add_to_head(self, value):
        # instanciating a new node
        new_node = Node(value=value)
        self.length += 1
        # Checking to look
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            # now assigning the new node to the head
            self.head = new_node

    def remove_head(self): # Taking the head off and then assing new head
        """ 
            Function will return The head value.  If there is no value then 
            it will return None
        """
        if self.length == 0:
            return None # will return -
        # getting the value of the head that is being removed
        theValue = self.head.value
        # This is the value that will be assigned to the head
        new_head = self.head.next_node
        # assigning the new_head
        self.head = new_head
        # if there is only one Node then we will need to set the tail
        if self.length == 1:
            self.tail = None
        # decrementing the length
        self.length -= 1

        return theValue


    def contains(self, searchValue):
        if self.length == 0:
            return False
        else:
            theNode = self.head 
            # Will start at the head and then traverse the list
            while theNode != None:
                if theNode.value == searchValue:
                    return True
                else: # will now increment to the next_node
                    theNode = theNode.next_node
            return False

    # This is the function that will get the maximun of the  linked list
    def get_max(self):
        # if the linked list has a lenght of 0 will return None
        if self.length == 0:
            return None
        val = self.head.value
        node = self.head
        while True:
            if node.value > val:
                val = node.value
            # move to the next node
            node = node.next_node
            if node == None:
                return val
           