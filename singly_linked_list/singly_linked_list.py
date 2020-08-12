class Node:
    def __init__(self, value, next_node=None):
        # this is the valye that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    # adding a method to get the value of the node
    def get_value(self):
        return self.value

    # method to get the node's 'next_node'
    def get_next(self):
        return self.next_node

    # method to update the node's 'next_node' to the input node
    def set_next(self, new_next):
        self.next_node = new_next



# 5 -> 7 -> 18 -> 22 -> 3 -> N
#  the number plus the error is what is needed for the node

# In order to add to the end we need to define another class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)
        # # check if there is no head
        # if not self.head:
        #     self.head = new_node
        #     self.tail = new_node
        # else: 
        #     self.tail.set_next(new_node)
        #     self.tail = new_node

    #  how we did it in class
        # wrap the value in the node
        self.value = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set head and tial to the new node
            self.head = new_node
            self.tail = new_node
            # otherwise, the list has at least one node
        else:
                # update the last(tail) node's 'next_node' to the new node
                self.tail.set_next(new_node)
                # update 'self.tail' to point to the new node we just added
                self.tail = new_node

    def remove_head(self):
        # is there a head
        if not self.head:
            return None

        # if head has no next, there is a single element in the linked list 
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        #set the head reference to the current head's next node in the list
        value = self.head.get_value()
        self.head = self.head.get_next()


        return value

    #     # Removing from the Head
    # def remove_head(self):
    #     # check if the linked list is empty
    #     if self.head is None and self.tail is None:
    #         return None
    #     # check if there is only one linked list node
    #     if self.head == self.tail:
    #         val = self.head.get_value()
    #         self.head = None
    #         self.tail = None
            
    #     else:
    #     # store the old heads value that we need to return
    #         val = self.head.get_value()
    #     # set 'self.head' to the old head's next node
    #     self.head = self.head.get_next()
    #     # return the old_heads value
    #     return val

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node, we are going to remove value
            val = self.head.get_value()

            self.head = None
            self.tail = None
            return val
        # otherwise, the linked list has more than one node
        else: 
        # store the last Node's value in another variable so we can return it
            val = self.tail.get_value()
        # we need to set 'self.tail' to the second to last Node
        # the only way we can do this, is by traversing the whole linkedlist from beginning

        # starting from the head, we'll traverse down to the second-to-last Node
        # init another reference to keep track of where we are in the linked list as were iterating
        current = self.head
        # keep iterating until the node after 'current' is tail
        while current.get_next() != self.tail:

            # keep iterating
            # set current to its own next
            current = current.get_next()

        # set 'self.tail' to 'current'
        self.tail = current

        # set the new tail's next_node to None
        self.tail.set_next(None)
        return val


    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node w're currently at; update this as we travers the linked list
        current = self.head
        # check to see if we're at a valid node
        while current:
            if current.get_value() == value:
                return True
        # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False
