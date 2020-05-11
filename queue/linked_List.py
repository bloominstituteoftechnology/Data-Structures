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
        # first node in the list
        self.head = None


    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)
        # what if the list is empty?
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # the last node in the list
            # we can get to the last node in the list by traversing it
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list
            current.set_next(new_node)


    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value

    def remove_at_end(self):
        current = self.head
        # what if the list is empty?
        if not current:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
        if previous is not None:
            previous.next_node = None
        else:
            self.head = None
        value = current.get_value()

        return value