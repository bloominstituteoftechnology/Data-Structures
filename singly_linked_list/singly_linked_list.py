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

    def add_to_head(self, value):
        # wrap the input value in a node
        new_node = Node(value)
        # check if the linked list is empty
        if not self.head and not self.tail:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the head
        else:
            # set the new node's `next` to refer to the current head
            new_node.set_next(self.head)
            # set the list's head reference to the new node
            self.head = new_node



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

    def get_max(self):
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

    def printLL(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.get_next()



"""
Ran 3 tests in 0.000s

OK
"""

ll = LinkedList()
# ll.add_to_head = Node(1)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

ll.add_to_tail(n1)
ll.add_to_tail(n2)
ll.add_to_tail(n3)
ll.add_to_tail(n4)
ll.add_to_tail(n5)
ll.add_to_tail(n6)

print(ll.printLL())

print(ll.tail)

print(ll.remove_tail)
print(ll.remove_head)