# linear data structure made up of nodes and refs to the next node

# lets make some node class
class Node:
    def __init__(self, value, next_node = None):
        # value that the node is holding
        self.value = value
        # ref to the next node in the chain
        self.next_node = next_node

    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)

# n1.set_next(n2) # n1.next_node = ne
# n2.get_value() # => (n2)

# now lets think of how we can make nodes interact in a way that consolidates their pieces together

# lets make a LinkedList class
# think of the idea of having a head and a tail like a snake
# where the snake can grow based upon having more links in it

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the value in a new Node
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise the list must have at least one item in there
        else:
            # update the Last node's "next_node" to the new node
            self.tail.set_next(new_node) # (Last node in chain).next_node = new_node
            # update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    def remove_tail(self):
        """
        remove the last node in the chain and return its value
        """
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if there is only one Node
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # remove the node
            # set head and tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        # otherwise
        else:
            # store the value of the node that we are going to remove
            value = self.tail.get_value()
            # we need to set the "self.tail" to the second to last node
            # we can only do this by traversing the whole list from beginning to end

            #start from the head
            current_node = self.head

            # keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                # keep looping
                current_node = current_node.get_next()

            # at the end of the iteration set "self.tail" to the current node
            self.tail = current_node
            # set the new tail's "next_node" to None
            self.tail.set_next(None)
            # return value
            return value


    def remove_head(self):
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # check if there is only one Node
        if self.head == self.tail:
            # store the value of the node that we are going to remove
            value = self.head.get_value()
            # remove the node
            # set head and tail to None
            self.head = None
            self.tail = None
            # return the stored value
            return value
        # otherwise
        else:
            # store the old head's value
            value = self.head.get_value()
            # set self.head to old head's next
            self.head = self.head.get_next()
            # return the value
            return value

