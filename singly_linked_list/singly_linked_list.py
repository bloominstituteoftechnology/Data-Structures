# create a Node Class
class Node:
    def __init__(self, value=None, next_node=None):
        # set the initial value of our node
        self.value = value

        # set a ref to the next node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node



class LinkedList:
    def __init__(self):
        # ref to head of list
        self.head = None
        #ref to tail of list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a new node
        new_node = Node(value, None)

        # check if there is no head (is the list empty)
        if not self.head:
            # if it is empty then we will set both the head and the tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise (we have a non empty list)
        else:
            # set the current tails next ref to our new node
            self.tail.next = new_node
            # set lists tail ref to our new node
            self.tail = new_node

    def remove_head(self):
        # if the list is empty then return None
        if not self.head:
            return None

        # if the head has no next (single element)
        if not self.head.get_next():
            # get a ref to the current head
            head = self.head
            # del the lists head ref
            self.head = None
            # make sure we set tail ref to None
            self.tail = None

            # return the value of the current heads next
            return head.get_value()
        
        # otherwise we have more than one element in our list
        # store the value
        value = self.head.get_value()
        # set the head ref to the current heads next node in the list
        self.head = self.head.get_next()
        # return the stored value
        return value


    def contains(self, value):
        # if there is no head we have an empty list
        if not self.head:
            # return None
            return None

        # get ref to the current node and this will be update when we traverse
        current_node = self.head

        # iterate over the list while current is not None
        while current_node:
            # if current value matches target value
            if current_node.get_value() == value:
                # return True
                return True
            # update our current node to the current nodes next (increment node)
            current_node = current_node.get_next()

        # return False
        return False