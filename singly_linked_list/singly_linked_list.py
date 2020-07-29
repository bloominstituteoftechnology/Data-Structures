"""
Node and LinkedList classes from our lecture discussion
"""
class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head       = None
        # reference to the tail of the list
        self.tail       = None
        # reference to the length of the list
        self.lgth       = 0
        # reference a value dict
        self.val_occr   = {}

    def occr_ctr_inc(self, val):
        if val not in self.val_occr:
            self.val_occr[val] = 1
            return

        self.val_occr[val] = self.val_occr[val] + 1
        return

    def occr_ctr_dec(self, val):
        if val not in self.val_occr:
            # error condition
            print("error condition 1")
            return

        if self.val_occr[val] == 1:
            del self.val_occr[val]
            return

        self.val_occr[val] = self.val_occr[val] - 1
        return


    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)

        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

        # Increment the length of the list
        self.lgth = self.lgth + 1
        self.occr_ctr_inc(value)

    def add_at_head(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)

        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node

        # we have a non-empty list, add the new node to the tail
        else:
            # the new node now becomes the head
            # the new node should point to the current head
            new_node.next_node = self.head
            # the head should refer to the new node
            self.head = new_node

        # Increment the length of the list
        self.lgth = self.lgth + 1
        self.occr_ctr_inc(value)

    def remove_head(self):
        # return None if there is no head
        if not self.head:
            return None

        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head

            # delete the list's head reference
            self.head = None

            # also make sure the tail reference doesn't refer to anything
            self.tail = None

            # just removed the single element so set length to zero
            self.lgth = 0
            # return the value
            self.occr_ctr_dec(head.get_value())
            return head.get_value()

        # otherwise we have more than one element in our list
        value = self.head.get_value()

        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()

        # decrement the length of the list
        self.lgth = self.lgth - 1
        self.occr_ctr_dec(value)
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head

        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True

            # update our current node to the current node's next node
            current = current.get_next()

        # if we've gotten here, then the target node isn't in our list
        return False

    def get_length(self):
        return self.lgth

    def get_max(self):
        # Convert the occurrence dict to a list
        if len(self.val_occr) == 0:
            return None
        
        list_keys = list(self.val_occr.keys())
        if len(list(list_keys)) == 0:
            return None

        print("list_keys is: ", type(list_keys))

        list_srtd = sorted(list_keys, reverse=True)
        return list_srtd[0]
